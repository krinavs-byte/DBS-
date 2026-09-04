from flask import Blueprint, render_template, request, jsonify, session, current_app, abort
from db import db, User, DashboardLayout
from functools import wraps
from jsonschema import validate, ValidationError
import json
import os

# blueprint
dashboard_bp = Blueprint("dashboard", __name__)

# Load JSON schema
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "docs", "schemas", "dashboard_layout.schema.json")
if not os.path.exists(SCHEMA_PATH):
    # allow top-level docs path in repo root if blueprint is run from root
    SCHEMA_PATH = os.path.join(os.getcwd(), "docs", "schemas", "dashboard_layout.schema.json")
with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    LAYOUT_SCHEMA = json.load(f)

def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            abort(401)
        return f(*args, **kwargs)
    return wrapped

@dashboard_bp.route("/app/dashboard")
@login_required
def view_dashboard():
    user_id = session.get("user_id")
    role = session.get("role", "user")
    layout = DashboardLayout.query.filter_by(user_id=user_id).order_by(DashboardLayout.updated_at.desc()).first()
    if not layout:
        # fallback to role-default
        layout = DashboardLayout.query.filter_by(role=role).order_by(DashboardLayout.updated_at.desc()).first()

    layout_json = layout.layout_json if layout else {"panels": [{"id": "kpi_strip", "position": {"x":0,"y":0,"w":12,"h":1}}]}
    return render_template("dashboard.html", layout_json=layout_json)

#
# API endpoints
#

@dashboard_bp.route("/api/dashboard/layouts/current", methods=["GET"])
@login_required
def api_get_current_layout():
    user_id = session.get("user_id")
    role = session.get("role", "user")
    layout = DashboardLayout.query.filter_by(user_id=user_id).order_by(DashboardLayout.updated_at.desc()).first()
    if not layout:
        layout = DashboardLayout.query.filter_by(role=role).order_by(DashboardLayout.updated_at.desc()).first()
    if not layout:
        return jsonify({"id": None, "layout_json": None, "version": None}), 404
    return jsonify({
        "id": layout.id,
        "user_id": layout.user_id,
        "role": layout.role,
        "layout_json": layout.layout_json,
        "version": layout.version,
        "updated_at": layout.updated_at.isoformat() if layout.updated_at else None
    })

@dashboard_bp.route("/api/dashboard/layouts", methods=["POST"])
@login_required
def api_create_layout():
    user_id = session.get("user_id")
    payload = request.get_json()
    if not payload or "layout_json" not in payload:
        return jsonify({"error": "missing_payload"}), 400
    layout_json = payload["layout_json"]

    # validate against schema
    try:
        validate(instance=layout_json, schema=LAYOUT_SCHEMA)
    except ValidationError as e:
        return jsonify({"error": "invalid_layout", "message": str(e)}), 400

    new_layout = DashboardLayout(user_id=user_id, layout_json=layout_json, version=1)
    db.session.add(new_layout)
    db.session.commit()
    return jsonify({"id": new_layout.id, "version": new_layout.version}), 201

@dashboard_bp.route("/api/dashboard/layouts/<int:layout_id>", methods=["PUT"])
@login_required
def api_update_layout(layout_id):
    user_id = session.get("user_id")
    payload = request.get_json()
    if not payload or "layout_json" not in payload or "version" not in payload:
        return jsonify({"error": "missing_payload"}), 400

    layout_json = payload["layout_json"]
    client_version = payload["version"]

    # validate JSON
    try:
        validate(instance=layout_json, schema=LAYOUT_SCHEMA)
    except ValidationError as e:
        return jsonify({"error": "invalid_layout", "message": str(e)}), 400

    layout = DashboardLayout.query.get(layout_id)
    if not layout:
        return jsonify({"error": "not_found"}), 404

    # ownership check: allow if user's layout or role-default update by manager
    if layout.user_id is not None and layout.user_id != user_id:
        return jsonify({"error": "forbidden"}), 403
    if layout.user_id is None:
        # role-default: only manager allowed to update
        if session.get("role") != "manager":
            return jsonify({"error": "forbidden_role_default"}), 403

    # optimistic locking
    if layout.version != client_version:
        return jsonify({
            "error": "stale",
            "message": "layout has changed",
            "current_version": layout.version,
            "current_layout": layout.layout_json
        }), 409

    # commit new layout
    layout.layout_json = layout_json
    layout.version = layout.version + 1
    db.session.add(layout)
    db.session.commit()
    return jsonify({"id": layout.id, "version": layout.version}), 200

@dashboard_bp.route("/api/panels/<panel_id>", methods=["GET"])
@login_required
def api_panel(panel_id):
    # stubbed panel payloads — replace with real logic that queries DB or services
    if panel_id == "kpi_strip":
        payload = {
            "total_skus": 120,
            "pending_transfers": 3,
            "alerts": 5
        }
    elif panel_id == "stock_alerts":
        payload = {
            "alerts": [
                {"sku": "SKU-1042", "name": "Steel Bolts", "days_left": 2, "severity": "critical"},
                {"sku": "SKU-2291", "name": "Packing Tape", "days_left": 4, "severity": "low"}
            ]
        }
    else:
        payload = {"message": f"panel {panel_id} not implemented yet"}

    return jsonify(payload)

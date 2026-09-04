from flask import Blueprint, render_template, request, redirect, url_for, session, current_app, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from db import db, User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html")

@auth_bp.route("/login", methods=["POST"])
def login_post():
    # supports form-encoded or JSON payloads
    if request.is_json:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
    else:
        email = request.form.get("email")
        password = request.form.get("password")

    if not email or not password:
        return jsonify({"ok": False, "error": "missing_credentials"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"ok": False, "error": "invalid_credentials"}), 401

    session.clear()
    session["user_id"] = user.id
    session["role"] = user.role

    # redirect or JSON
    if request.is_json:
        return jsonify({"ok": True, "redirect": url_for("dashboard.view_dashboard")})
    return redirect(url_for("dashboard.view_dashboard"))

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login_get"))

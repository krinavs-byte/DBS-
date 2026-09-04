"""
Seed script for local development.

Creates:
- sqlite dev.db (via SQLAlchemy create_all)
- admin user (admin@example.com / passw0rd)
- a role-default layout for 'user'
"""
from db import db, User, DashboardLayout
from app import create_app
from werkzeug.security import generate_password_hash
import os
import json

app = create_app()
app.app_context().push()

db.create_all()

# create admin if not exists
admin_email = "admin@example.com"
admin = User.query.filter_by(email=admin_email).first()
if not admin:
    admin = User(email=admin_email, password_hash=generate_password_hash("passw0rd"), role="manager")
    db.session.add(admin)
    db.session.commit()
    print("Created admin:", admin_email, "password: passw0rd")
else:
    print("Admin exists:", admin_email)

# create a role-default layout if none exists
existing = DashboardLayout.query.filter_by(role="user").first()
if not existing:
    sample_layout = {
        "panels": [
            {"id": "kpi_strip", "position": {"x":0,"y":0,"w":12,"h":1}},
            {"id": "stock_alerts", "position": {"x":0,"y":1,"w":6,"h":6}},
            {"id": "transfers", "position": {"x":6,"y":1,"w":6,"h":6}}
        ]
    }
    rl = DashboardLayout(user_id=None, role="user", layout_json=sample_layout, version=1)
    db.session.add(rl)
    db.session.commit()
    print("Created role-default user layout")
else:
    print("Role-default user layout exists")

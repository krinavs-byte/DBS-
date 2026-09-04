import pytest
import json
from app import create_app
from db import db, User, DashboardLayout
from werkzeug.security import generate_password_hash

@pytest.fixture
def client(tmp_path, monkeypatch):
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            db.init_app(app)
            db.create_all()
            # create user
            u = User(email="u@example.com", password_hash=generate_password_hash("pw"), role="user")
            db.session.add(u)
            db.session.commit()
        yield client

def login(client):
    resp = client.post("/login", json={"email":"u@example.com","password":"pw"})
    assert resp.status_code == 200

def test_create_and_update_layout(client):
    login(client)
    # create layout
    payload = {"layout_json": {"panels":[{"id":"kpi_strip","position":{"x":0,"y":0,"w":12,"h":1}}]}}
    r = client.post("/api/dashboard/layouts", json=payload)
    assert r.status_code == 201
    body = r.get_json()
    lid = body["id"]

    # get current layout
    r2 = client.get("/api/dashboard/layouts/current")
    assert r2.status_code == 200
    current = r2.get_json()
    assert current["id"] == lid

    # update with correct version
    upd = {"layout_json": {"panels":[{"id":"kpi_strip","position":{"x":0,"y":0,"w":6,"h":1}}]}, "version": current["version"]}
    r3 = client.put(f"/api/dashboard/layouts/{lid}", json=upd)
    assert r3.status_code == 200

    # stale update should return 409
    r4 = client.put(f"/api/dashboard/layouts/{lid}", json=upd)
    assert r4.status_code == 409

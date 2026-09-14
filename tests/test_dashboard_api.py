import json
from app import create_app
from db import db, User, DashboardLayout
import pytest

@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with app.app_context():
        db.create_all()
        # create a test user
        user = User(email="test@example.com", password_hash="noop", role="user")
        db.session.add(user)
        db.session.commit()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()


def test_get_current_layout_requires_auth(client):
    res = client.get('/api/dashboard/layouts/current')
    assert res.status_code in (401, 404)

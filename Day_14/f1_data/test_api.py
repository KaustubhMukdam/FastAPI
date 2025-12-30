from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import main as f1_main
from . import database as f1_database
from .database import Base, get_db
import os
from dotenv import load_dotenv

load_dotenv()


SQLALCHEMY_DATABASE_URL = os.getenv("SQLite_F1_Database_URL", "sqlite:///./f1data.db")

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


Base.metadata.create_all(bind=engine)

f1_main.app.dependency_overrides[get_db] = override_get_db

client = TestClient(f1_main.app)


def test_create_and_get_driver():
    resp = client.post("/drivers/", json={"name": "Test Driver", "team": "Test Team", "points": 42})
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "Test Driver"
    driver_id = data["id"]

    resp2 = client.get(f"/drivers/{driver_id}")
    assert resp2.status_code == 200
    assert resp2.json()["id"] == driver_id


def test_update_and_delete_driver():
    resp = client.post("/drivers/", json={"name": "To Update", "team": "T", "points": 1})
    assert resp.status_code == 201
    driver_id = resp.json()["id"]

    resp2 = client.put(f"/drivers/{driver_id}", json={"name": "Updated", "team": "T2", "points": 10})
    assert resp2.status_code == 200
    assert resp2.json()["name"] == "Updated"

    resp3 = client.delete(f"/drivers/{driver_id}")
    assert resp3.status_code == 200

    resp4 = client.get(f"/drivers/{driver_id}")
    assert resp4.status_code == 404

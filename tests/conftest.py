from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi.testclient import TestClient

import pytest

from database.database import Base
from database.database import get_db

from main import app



SQLALCHEMY_DATABASE_URL = (
    "sqlite:///./test.db"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Override Dependency
def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db

    finally:
        db.close()


app.dependency_overrides[
    get_db
] = override_get_db


# Test Client Fixture
@pytest.fixture
def client():
     # Drop and recreate all tables before each test 
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    return TestClient(app)



# Reusable fixture: gives you an authenticated token
@pytest.fixture
def auth_token(client):
    client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "email": "test1@example.com",
            "password": "password123"
        }
    )
    response = client.post(
        "/auth/login",
        data={
            "username": "test1@example.com",
            "password": "password123"
        }
    )
    return response.json()["access_token"]
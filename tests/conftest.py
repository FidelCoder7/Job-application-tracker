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

Base.metadata.create_all(bind=engine)


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
    return TestClient(app)

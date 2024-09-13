import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session

from backend.app import app
from backend.database.get_session import get_session
from backend.database.models import table_registry
from backend.security import Hasher

from . import factories


@pytest.fixture
def client(session):
    def session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def user(session):
    pwd = 'testtest'
    user = factories.UserFactory(password=Hasher.get_password_hash(pwd))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.plain_pwd = pwd

    return user

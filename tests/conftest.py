import pytest
from fastapi.testclient import TestClient

from track_my_attendance.app import app


@pytest.fixture
def client():
    return TestClient(app)

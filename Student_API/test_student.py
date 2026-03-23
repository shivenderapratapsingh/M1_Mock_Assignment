import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def student_data():
    return {
        "s_name": "Test",
        "s_age": 20,
        "s_course": "AI",
        "s_college": "XYZ"
    }

def test_create_student(student_data):

    response = client.post("/students", json=student_data)

    assert response.status_code == 200 or response.status_code == 201

    data = response.json()

    assert data["s_name"] == "Test"


def test_get_students():

    response = client.get("/students")

    assert response.status_code in [200,404]
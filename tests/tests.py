from fastapi.testclient import TestClient
from cicd_test.main import app

service_test = TestClient(app=app)


def main_dev():
    response = service_test.get('/')
    assert response.status_code == 200, "Error status code"
    assert response.json() == "Hello world"


def get_my_id():
    response = service_test.get(f"/get_id/{12}/")
    assert response.json().get('pk') == 12


def test_main_function():
    main_dev()
    get_my_id()


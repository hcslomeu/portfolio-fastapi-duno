from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_root_returns_hello_world():
    """
    This test have 3 steps (AAA)
    - A: Arrange
    - A: Act
    - A: Assert
    """
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}

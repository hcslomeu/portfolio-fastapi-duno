from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app

# client = TestClient(app)


def test_read_root():
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


def test_new_page():
    client = TestClient(app)

    response = client.get('/test_html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Hello world! </h1>' in response.text

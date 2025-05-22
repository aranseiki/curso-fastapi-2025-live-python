from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Olá, mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_hello_deve_retornar_html():
    client = TestClient(app)

    response = client.get('/hello')

    assert response.text == """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta
                name="viewport"
                content="width=device-width,
                initial-scale=1.0"
            >
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
        </html>
    """
    assert response.status_code == HTTPStatus.OK

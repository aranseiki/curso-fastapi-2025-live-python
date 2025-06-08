from http import HTTPStatus

import pytest

from fastapi_zero.app import read_hello, read_root


@pytest.mark.asyncio
async def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')
    response_ola_mundo = await read_root()

    assert response.json() == {'message': 'Olá, mundo!'}
    assert response.status_code == HTTPStatus.OK
    assert response.json() == response_ola_mundo


@pytest.mark.asyncio
async def test_hello_deve_retornar_html(client):
    response = client.get('/hello')
    response_hello = await read_hello()

    assert (
        response.text
        == """
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
    )
    assert response.status_code == HTTPStatus.OK
    assert response.text == response_hello

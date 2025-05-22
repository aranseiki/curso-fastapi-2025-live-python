from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='FastAPI Zero')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, mundo!'}


@app.get('/hello', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_hello():
    return """
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

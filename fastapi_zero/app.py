from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='Mock API')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World!'}


@app.get('/test_html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def new_page():
    return """
    <html>
      <head>
        <title>New page!</title>
      </head>
      <body>
        <h1> Hello world! </h1>
      </body>
    </html>"""

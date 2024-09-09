from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Ola, mundo'}


@app.post('/')
def o():
    return print('lçsdfsdllfçsdç')


# fastapi documenta a sua API automaticamente, por meio de /docs e /redoc
# ruff garante analisa a formatação do código de acordo com boas práticas.
# taskipy
#
#
#
#
#

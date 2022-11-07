from fastapi import FastAPI

app = FastAPI()

posts = []

#Declaramos ruta principal del api
@app.get('/')
def read_root():
    """
    Devuelve un diccionario con clave "bienvenido" y valor "Bienvenidos a mi api"
    :return: Un diccionario con una clave y un valor.
    """
    return {"bienvenido": "Bienvenidos a mi api"}

@app.get('/post')
def posts():
    return posts
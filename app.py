from fastapi import FastAPI, HTTPException
from model import Post

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

@app.get('/posts')
def get_posts():
    """
    Devuelve la variable de publicaciones.
    :return: Una lista de diccionarios.
    """
    return posts

@app.post('/posts')
def save_post(post: Post):
    """
    Toma un objeto Publicar, lo convierte en un diccionario y lo agrega a la lista de publicaciones.
    
    :param post: Correo
    :type post: Post
    :return: El último elemento de la lista.
    """
    posts.append(post.dict())
    return posts[-1]


@app.get('/posts/{id}')
def get_post(id: str):
    """
    Si la identificación de la publicación es igual a la identificación pasada, devolver la publicación
    
    :param id: id de la publicación
    :type id: str
    :return: Una publicación
    """
    for post in posts:
        print(post)
        if str(post['id']) == id:
            return post
    
    raise HTTPException(status_code=404, detail="Post no encontrado")

@app.delete('posts/{id}')
def update_post(id: str):
    """
    Si la identificación de la publicación coincide con la identificación de la publicación en la lista,
    actualice el título, el contenido y el autor de la publicación.
    
    :param id: calle
    :type id: str
    :return: Un diccionario con un mensaje.
    """
    for index, post in enumerate(posts):
        if str(post['id']) == id:
            posts[index]["title"] = data.title
            posts[index]["content"] = data.content
            posts[index]["author"] = data.author

            return {"message": "Post actualizado correctamente"}

    raise HTTPException(status_code=404, detail="Post no encontrado")


@app.delete('posts/{id}')
def delete_post(id: str):
    """
    Recorre la lista de publicaciones y, si la identificación de la publicación coincide con la
    identificación pasada, elimina la publicación de la lista y devuelve un mensaje.
    
    :param id: calle
    :type id: str
    :return: Un diccionario con un mensaje.
    """
    for index, post in enumerate(posts):
        if str(post['id']) == id:
            posts.pop(index)
            return {"message": "Post eliminado correctamente"}

    raise HTTPException(status_code=404, detail="Post no encontrado")
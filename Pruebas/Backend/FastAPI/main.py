from fastapi import FastAPI

from pydantic import BaseModel


# BaseModel

app = FastAPI()


@app.get("/")
async def root():              # async indica que no hay que esperar que el server conteste para que siga el código ejecutando, porque igual tarda más o meno, esperando a que vengan los datos
    return "¡Hola FastAPI!"


@app.get("/url")
async def url ():
    return {"url_curso":"https://mouredev.com/python"}


## Arrancar el server local para testeo

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1,name="Brais",surname="Moure",url="http://telita.com",age=34),
              User(id=2,name="Jesús",surname="Gómez",url="http://twitter.com/Jesusocu",age=29),
              User(id=3, name="Javier",surname="Ocaña",url="http://twitter.com/Javiocu",age=28),
              User(id=4, name="Abdul",surname="Ramal",url="http://twitter.com/AbduliTo",age=46)]


@app.get("/usersjson")
async def usersjson():
    return [{"name":"Javier","surname":"Ocaña","url":"http://twitter.com/Javiocu","age": 28},
            {"name":"Jesús","surname":"Ocaña","url":"http://twitter.com/Jesusocu","age":29},
            {"name":"Abdul","surname":"Ramal","url":"http://twitter.com/AbduliTo","age":46}]


@app.get("/lista/")
async def vuelta():
    return users_list

    

# Query                                  Con query se dice cuando se usa ? en la barra delante de la clave que quieras buscar, este caso id
@app.get("/user/")
async def usersa(id:int):
    return search_user(id)

# Path
@app.get("/user/{id}")
async def users(id:int):
    return search_user(id)
    


# Post

@app.post("/user/")
async def user(vale: User):
    if type(search_user(vale.id)) == User:
        return f"El usuario con id: {vale.id} ya existe"
    else:
        users_list.append(vale)
        return f"Todo bien, se ha añadido el usurario con id: {vale.id}"



def search_user(id):
    users = filter(lambda user: user.id == id , users_list)
    try:
        return list(users)[0]
    except:
        return f"No se ha encontrado un User con el id:{id}"
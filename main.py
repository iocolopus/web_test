from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class User(BaseModel):
    user : str
    password : str

app = FastAPI()

# Configura los orígenes permitidos (puedes ajustar según tus necesidades)
origins = ["*"]

# Agrega el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

usuarios = [User(user = "Default",password = "default")]

@app.get("/")
async def root():
    return usuarios

@app.post("/registrar")
async def root(usuario : User):
    user = usuario.user
    password = usuario.password

    if not list(filter(lambda x: x.user == user, usuarios)):
        usuarios.append(usuario)
        return {"success" : True, "message": "Se ha creado un nuevo usuario"}
    else:
        return {"success" : False, "message": "El usuario que se ha intentado crear ya esta en la base da datos"}

@app.post("/entrar")
async def entrar(usuario : User):
    user = usuario.user
    password = usuario.password

    if list(filter(lambda x: x.user == user and x.password == password, usuarios)):
        return {"success" : True, "message": "Se ha autentificado con exito"}
    else:
        return {"success" : False, "message": "No se ha podifo autentificar"}
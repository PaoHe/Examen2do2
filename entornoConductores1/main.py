from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from models import modeloUsuario

app = FastAPI(
    title = 'Registro Conductores',
    descripcion = 'Paola',
    version = '1.0.1'
)

class modeloUsuario(BaseModel):
    id : int
    Licencia : str
    Conductor : str
    Numero : str

licencias = [
    {"id" : 1, "Licencia": "A","Conductor":"Paola","Numero":"AAAA1111AAAA"},
    {"id" : 2, "Licencia": "B","Conductor":"Juan","Numero":"BBBB2222BBBB"},
    {"id" : 3, "Licencia": "C","Conductor":"Monica","NNumero":"CCCC3333CCCC"},
    {"id" : 4, "Licencia": "D","Conductor":"Isay","Numero":"DDDD4444DDDD"},
]

#Conculta TODOS LOS CONDUCTORES
@app.get("/todasConductores")
def leerConductores():
    return {"Los conductores son":licencias}

#Endpoint ACTUALIZAR CONDUCTOR
@app.put("/actualizarConductor/{id}", response_model = modeloUsuario, tags=['Operaciónes CRUD'])
def actualizarConductor(id: int, ConductorActualizado:modeloUsuario):
    for index, usr in enumerate(licencias):
        if usr["id"] == id:
            licencias [index] = ConductorActualizado.model_dump()
            return licencias[index]
        raise HTTPException(status_code=400, detail="El usuario no existre")


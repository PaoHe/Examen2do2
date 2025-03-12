from pydantic import BaseModel, Field, EmailStr

#Modelo de validaciones
class modeloUsuario(BaseModel):
    id: int = Field(...,gt=0, description="ID unico y solo numeros positivos")
    Licencia: str = Field(...,min_length=0, max_length=1, description="Solo A,B,C,D")
    Conductor: str = Field(..., min_length=3, description="solo caracteres minimo 3")
    Numero: str = Field(...,min_length=12, max_length=12, description="!2 caracteres unicamente")
    
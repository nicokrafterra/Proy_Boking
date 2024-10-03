from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioBase(BaseModel):
    id: Optional[int] = None  
    nombre: str
    correoElectronico: str
    contraseñaUsuario: str
    numeroCelular: str
    edad: int
    esAdmin: bool = False

class ReservaU(BaseModel):
    id: Optional[int] = None
    usuario_id: int
    fecha: date
    tipo_Reserva: str
    pagada: bool = False
    
    


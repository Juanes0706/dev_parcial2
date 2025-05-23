from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum

class EstadoUsuario(str, Enum):
    activo = "Activo"
    inactivo = "Inactivo"
    eliminado = "Eliminado"

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str
    premium: bool = False
    estado: EstadoUsuario = Field(default=EstadoUsuario.activo)

class Tarea(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False
    usuario_id: int = Field(foreign_key="usuario.id")

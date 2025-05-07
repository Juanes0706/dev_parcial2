from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from utils.db import engine, crear_db, get_session
from data.models import Usuario, EstadoUsuario, Tarea
from operations.operations_db import (
    crear_usuario,
    obtener_usuarios,
    obtener_usuario_por_id,
    actualizar_usuario,
    eliminar_usuario,
    usuarios_por_estado,
    usuarios_premium_y_activos,
    crear_tarea,
    obtener_tareas,
    obtener_tarea_por_id,
    actualizar_tarea,
    eliminar_tarea,
    tareas_por_usuario
)

app = FastAPI()

@app.on_event("startup")
def startup():
    crear_db()


@app.post("/usuarios/", tags=["Usuarios"])
def crear(usuario: Usuario, session: Session = Depends(get_session)):
    return crear_usuario(session, usuario)

@app.get("/usuarios/", tags=["Usuarios"])
def listar(session: Session = Depends(get_session)):
    return obtener_usuarios(session)

@app.get("/usuarios/{id}", tags=["Usuarios"])
def ver(id: int, session: Session = Depends(get_session)):
    usuario = obtener_usuario_por_id(session, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.put("/usuarios/{id}", tags=["Usuarios"])
def actualizar(id: int, datos: Usuario, session: Session = Depends(get_session)):
    usuario = actualizar_usuario(session, id, datos)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.delete("/usuarios/{id}", tags=["Usuarios"])
def eliminar(id: int, session: Session = Depends(get_session)):
    usuario = eliminar_usuario(session, id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.get("/usuarios/estado/{estado}", tags=["Usuarios"])
def por_estado(estado: EstadoUsuario, session: Session = Depends(get_session)):
    return usuarios_por_estado(session, estado)

@app.get("/usuarios/premium/activos", tags=["Usuarios"])
def premium_activos(session: Session = Depends(get_session)):
    return usuarios_premium_y_activos(session)

@app.get("/usuarios/{usuario_id}/tareas", tags=["Usuarios"])
def tareas_de_usuario(usuario_id: int, session: Session = Depends(get_session)):
    tareas = tareas_por_usuario(session, usuario_id)
    if not tareas:
        raise HTTPException(status_code=404, detail="No se encontraron tareas para este usuario")
    return tareas


@app.post("/tareas/", tags=["Tareas"])
def crear_t(tarea: Tarea, session: Session = Depends(get_session)):
    return crear_tarea(session, tarea)

@app.get("/tareas/", tags=["Tareas"])
def listar_t(session: Session = Depends(get_session)):
    return obtener_tareas(session)

@app.get("/tareas/{id}", tags=["Tareas"])
def ver_t(id: int, session: Session = Depends(get_session)):
    tarea = obtener_tarea_por_id(session, id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@app.put("/tareas/{id}", tags=["Tareas"])
def actualizar_t(id: int, datos: Tarea, session: Session = Depends(get_session)):
    tarea = actualizar_tarea(session, id, datos)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

@app.delete("/tareas/{id}", tags=["Tareas"])
def eliminar_t(id: int, session: Session = Depends(get_session)):
    tarea = eliminar_tarea(session, id)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

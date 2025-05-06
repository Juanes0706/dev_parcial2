from sqlmodel import Session, select
from data.models import Usuario, EstadoUsuario, Tarea

# Operaciones de Usuario
def crear_usuario(session: Session, usuario: Usuario):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

def obtener_usuarios(session: Session):
    return session.exec(select(Usuario).where(Usuario.estado != EstadoUsuario.eliminado)).all()

def obtener_usuario_por_id(session: Session, id: int):
    return session.get(Usuario, id)

def actualizar_usuario(session: Session, id: int, datos: Usuario):
    usuario = session.get(Usuario, id)
    if usuario:
        usuario.nombre = datos.nombre
        usuario.email = datos.email
        usuario.premium = datos.premium
        session.commit()
        session.refresh(usuario)
    return usuario

def eliminar_usuario(session: Session, id: int):
    usuario = session.get(Usuario, id)
    if usuario:
        usuario.estado = EstadoUsuario.eliminado
        session.commit()
        session.refresh(usuario)
    return usuario

def usuarios_por_estado(session: Session, estado: EstadoUsuario):
    return session.exec(select(Usuario).where(Usuario.estado == estado)).all()

def usuarios_premium_y_activos(session: Session):
    return session.exec(
        select(Usuario).where(Usuario.estado == EstadoUsuario.activo, Usuario.premium == True)
    ).all()

# Operaciones de Tarea
def crear_tarea(session: Session, tarea: Tarea):
    session.add(tarea)
    session.commit()
    session.refresh(tarea)
    return tarea

def obtener_tareas(session: Session):
    return session.exec(select(Tarea)).all()

def obtener_tarea_por_id(session: Session, id: int):
    return session.get(Tarea, id)

def actualizar_tarea(session: Session, id: int, datos: Tarea):
    tarea = session.get(Tarea, id)
    if tarea:
        tarea.titulo = datos.titulo
        tarea.descripcion = datos.descripcion
        tarea.completada = datos.completada
        tarea.usuario_id = datos.usuario_id
        session.commit()
        session.refresh(tarea)
    return tarea

def eliminar_tarea(session: Session, id: int):
    tarea = session.get(Tarea, id)
    if tarea:
        session.delete(tarea)
        session.commit()
    return tarea

def tareas_por_usuario(session: Session, usuario_id: int):
    return session.exec(select(Tarea).where(Tarea.usuario_id == usuario_id)).all()

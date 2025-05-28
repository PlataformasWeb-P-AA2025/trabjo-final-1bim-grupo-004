from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 1: Publicaciones de un usuario
def listar_publicaciones_usuario(nombre_usuario):
    usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    if usuario:
        return [(pub.id, pub.contenido) for pub in usuario.publicaciones[:10]]
    return []

# Ejecución
usuario_ejemplo = session.query(Usuario).first().nombre
print("→ Publicaciones del usuario:", listar_publicaciones_usuario(usuario_ejemplo))

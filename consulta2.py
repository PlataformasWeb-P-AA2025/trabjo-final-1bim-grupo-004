from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 2: Publicaciones en las que reaccionó un usuario
def publicaciones_reaccionadas_por_usuario(nombre_usuario):
    usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    if usuario:
        return [(r.publicacion.id, r.publicacion.contenido, r.emocion) for r in usuario.reacciones[:10]]
    return []

# Ejecución
usuario_ejemplo = session.query(Usuario).first().nombre
print("→ Publicaciones reaccionadas:", publicaciones_reaccionadas_por_usuario(usuario_ejemplo))

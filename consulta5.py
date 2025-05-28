from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 5: Reacciones a publicaciones propias
def usuarios_que_reaccionaron_a_sus_publicaciones():
    return session.query(Reaccion).join(Publicacion).filter(
        Reaccion.usuario_id == Publicacion.usuario_id
    ).limit(10).all()

# Ejecución
print("→ Usuarios que reaccionaron a sus propias publicaciones:", [
    (r.usuario.nombre, r.publicacion.contenido, r.emocion) for r in usuarios_que_reaccionaron_a_sus_publicaciones()])

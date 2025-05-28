from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

# Conexión a base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 1: Publicaciones de un usuario
def listar_publicaciones_usuario(nombre_usuario):
    usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    if usuario:
        return [(pub.id, pub.contenido) for pub in usuario.publicaciones[:10]]
    return []

# Consulta 2: Publicaciones en las que reaccionó un usuario
def publicaciones_reaccionadas_por_usuario(nombre_usuario):
    usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    if usuario:
        return [(r.publicacion.id, r.publicacion.contenido, r.emocion) for r in usuario.reacciones[:10]]
    return []

# Consulta 3: Conteo de emociones
def contar_emociones():
    return session.query(Reaccion.emocion, func.count(Reaccion.emocion)).group_by(Reaccion.emocion).limit(10).all()

# Consulta 4: Reacciones específicas de usuarios que NO inician con vocal
def reacciones_filtradas_por_nombre_y_emocion():
    emociones_deseadas = ['alegre', 'enojado', 'pensativo']
    return session.query(Reaccion).join(Usuario).filter(
        ~Usuario.nombre.op('regexp')('^[AEIOUaeiou]'),
        Reaccion.emocion.in_(emociones_deseadas)
    ).limit(10).all()

# Consulta 5: Reacciones a publicaciones propias
def usuarios_que_reaccionaron_a_sus_publicaciones():
    return session.query(Reaccion).join(Publicacion).filter(
        Reaccion.usuario_id == Publicacion.usuario_id
    ).limit(10).all()

# Ejecutar ejemplo
usuario_ejemplo = session.query(Usuario).first().nombre
print("→ Publicaciones del usuario:", listar_publicaciones_usuario(usuario_ejemplo))
print("→ Publicaciones reaccionadas:", publicaciones_reaccionadas_por_usuario(usuario_ejemplo))
print("→ Conteo de emociones:", contar_emociones())
print("→ Reacciones no vocal y emoción filtrada:", [
    (r.usuario.nombre, r.publicacion.contenido, r.emocion) for r in reacciones_filtradas_por_nombre_y_emocion()])
print("→ Usuarios que reaccionaron a sus propias publicaciones:", [
    (r.usuario.nombre, r.publicacion.contenido, r.emocion) for r in usuarios_que_reaccionaron_a_sus_publicaciones()])

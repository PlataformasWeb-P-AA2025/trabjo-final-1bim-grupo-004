from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 4: Reacciones específicas de usuarios que NO inician con vocal
def reacciones_filtradas_por_nombre_y_emocion():
    emociones_deseadas = ['alegre', 'enojado', 'pensativo']
    return session.query(Reaccion).join(Usuario).filter(
        ~Usuario.nombre.op('regexp')('^[AEIOUaeiou]'),
        Reaccion.emocion.in_(emociones_deseadas)
    ).limit(10).all()

# Ejecución
print("→ Reacciones no vocal y emoción filtrada:", [
    (r.usuario.nombre, r.publicacion.contenido, r.emocion) for r in reacciones_filtradas_por_nombre_y_emocion()])

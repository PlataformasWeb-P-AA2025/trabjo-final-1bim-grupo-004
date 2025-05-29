from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

# se importan las clases del 
# archivo clases.py
from genera_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# 9.  Publicaciones que tienen más de una reacción

publicaciones_populares = session.query(
    Publicacion.contenido,
    func.count(Reaccion.id).label("total_reacciones")
).join(Publicacion.reacciones).group_by(Publicacion.id).having(func.count(Reaccion.id) > 1).all()

for contenido, total in publicaciones_populares:
    print(f"Publicación: '{contenido}' tiene {total} reacciones.")
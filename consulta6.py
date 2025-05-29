from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

# 6. Listar las reacciones a una publicacion
reacciones = session.query(Reaccion)\
    .join(Usuario)\
    .filter(Reaccion.publicacion_id == 4)\
    .all()

for reaccion in reacciones:
    print(f"Usuario: {reaccion.usuario.nombre}, Emocion: {reaccion.emocion}")

    


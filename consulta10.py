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

# 10. Usuarios que nunca han hecho una publicación

usuarios_sin_publicaciones = session.query(Usuario).outerjoin(Usuario.publicaciones).filter(Publicacion.id == None).all()

for usuario in usuarios_sin_publicaciones:
    print(f"{usuario.nombre} no ha hecho ninguna publicación.")


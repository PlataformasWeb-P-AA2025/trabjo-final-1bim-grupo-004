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

# 8. Usuarios con más de una publicación.

usuarios_con_muchas_publicaciones = session.query(
    Usuario.nombre,
    func.count(Publicacion.id).label("total_publicaciones")
).join(Usuario.publicaciones).group_by(Usuario.id).having(func.count(Publicacion.id) > 1).all()

for usuario, total in usuarios_con_muchas_publicaciones:
    print(f"{usuario} ha hecho {total} publicaciones.")
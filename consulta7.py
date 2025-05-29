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

# 7. Reporte de cuantas veces se ha usado cada tipo de reaccion

reacciones = session.query(
    Reaccion.emocion,
    func.count(Reaccion.emocion).label('total')
).group_by(Reaccion.emocion)\
    .all()

for emocion, total in reacciones:
    print(f"Emocion: {emocion}, Total: {total}")
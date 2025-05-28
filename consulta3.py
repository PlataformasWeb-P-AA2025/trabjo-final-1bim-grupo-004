from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 3: Conteo de emociones
def contar_emociones():
    return session.query(Reaccion.emocion, func.count(Reaccion.emocion)).group_by(Reaccion.emocion).limit(10).all()

# Ejecución
print("→ Conteo de emociones:", contar_emociones())

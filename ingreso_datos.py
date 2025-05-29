import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Usuario, Publicacion, Reaccion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de datos
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Leer CSVs
usuarios_df = pd.read_csv("DATA/usuarios_red_x.csv")
publicaciones_df = pd.read_csv("DATA/usuarios_publicaciones.csv")
emociones_df = pd.read_csv("DATA/usuario_publicacion_emocion.csv")

# Crear usuarios
for _, row in usuarios_df.iterrows():
    session.add(Usuario(nombre=row["usuario"]))

# Crear publicaciones
for _, row in publicaciones_df.iterrows():
    nombre_usuario, contenido = row["usuario|publicacion"].split("|", 1)
    
    usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    if usuario:
        session.add(Publicacion(contenido=contenido, usuario=usuario))

# Crear reacciones
for _, row in emociones_df.iterrows():
    nombre_usuario, comentario, emocion = row["Usuario|comentario|tipo emocion"].split("|", 2)

    usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()
    publicacion = session.query(Publicacion).filter_by(contenido=comentario).first()

    if usuario and publicacion:
        session.add(Reaccion(usuario=usuario, publicacion=publicacion, emocion=emocion))

session.commit()
print("Datos insertados exitosamente en la base de datos.")
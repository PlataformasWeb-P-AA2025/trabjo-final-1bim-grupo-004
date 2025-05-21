from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint, create_engine
from sqlalchemy.orm import relationship, declarative_base

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de datos
# para el taller se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(20), nullable=False)

    publicaciones = relationship("Publicacion", back_populates="usuario")
    reacciones = relationship("Reaccion", back_populates="usuario")

    def _repr_(self):
        return f"Usuario: id={self.id}, nombre={self.nombre}"

class Publicacion(Base):
    __tablename__ = 'publicaciones'
    id = Column(Integer, primary_key=True)
    contenido = Column(Text, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    usuario = relationship("Usuario", back_populates="publicaciones")
    reacciones = relationship("Reaccion", back_populates="publicacion")

    def _repr_(self):
        return f"Publicacion: id={self.id}, usuario_id={self.usuario_id}, contenido={self.contenido}"

class Reaccion(Base):
    __tablename__ = 'reacciones'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    publicacion_id = Column(Integer, ForeignKey('publicaciones.id'), nullable=False)
    emocion = Column(String, nullable=False)

    usuario = relationship("Usuario", back_populates="reacciones")
    publicacion = relationship("Publicacion", back_populates="reacciones")

    __table_args__ = (UniqueConstraint('usuario_id', 'publicacion_id', name='uix_usuario_publicacion'),)

    def _repr_(self):
        return f"Reaccion: usuario_id={self.usuario_id}, publicacion_id={self.publicacion_id}, emocion={self.emocion}"

Base.metadata.create_all(engine)

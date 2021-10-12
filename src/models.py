import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    altura = Column(Integer)
    sexo = Column(String(250))
    planetanatal =  Column(Integer, ForeignKey('planeta.nombre'))  

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    diametro = Column(Integer)
    poblacion = Column(Integer)
    clima = Column(String(100))
    vinculoPersonaje = relationship("Personaje")

class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    piloto_uid = Column(Integer, primary_key=True)
    nombre = Column(String(80), ForeignKey('personaje.nombre'), nullable=False)
    vinculoVehiculo = relationship("Personaje")

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    personaje = Column(String(50), ForeignKey('personaje.nombre'))
    planeta = Column(String(50),ForeignKey('planeta.nombre'))
    vehiculo = Column(String(50),ForeignKey('vehiculo.nombre'))

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    usuario_nombre = Column(String(50),ForeignKey('favoritos'))
    contraseña = Column(String(50))
    vinculoUsuario = relationship("Favoritos")

   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
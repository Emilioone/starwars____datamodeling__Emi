import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ ='user'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    email= Column(String(250), nullable=False, unique=True)
    userName = Column(String(80), nullable=False, unique=True)
    password= Column(String(250), nullable=False)
    favorites = relationship("Favorite", uselist=True, backref='user') 


class Planet(Base):
    __tablename__='planet'
    id = Column(Integer, primary_key=True)
    nombre_planeta = Column(String(80), nullable=False)
    poblacion = Column(String(250), nullable=False)
    favorites = relationship("Favorite", ForeignKey("favorites.id"))

class Vehicle(Base):
    __tablename__= 'vehiculos'
    id= Column(Integer, primary_key=True)
    vehicle_type = Column(String(80), nullable=False)
    color = Column(String(80), nullable=False)
    favorites = relationship("Favorite", ForeignKey("favorites.id"))   


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    color_ojos = Column(String(250), nullable =False)
    favorites = relationship("Favorite", ForeignKey("favorites.id"))


class Favorite(Base):
    __tablename__= 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer(), ForeignKey("user.id"))
    planeta_id = Column(Integer(), ForeignKey("planet.id"))
    people_id = Column(Integer(), ForeignKey("people.id"))
    vehiculos_type = Column(String(80), ForeignKey("vehicle.vehicle_type"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

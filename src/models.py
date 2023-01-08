import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.sql.sqltypes import Enum
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Enum


Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)  # Set primary key
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)

class Favorites(Base):
    __tablename__ = 'Favorites'
    user_id = Column(Integer, ForeignKey('Users.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('Characters.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('Planets.id'), primary_key=True)
    character = relationship("Character")
    planet = relationship("Planet")

class Character(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    mass = Column(Integer)
    height = Column(Integer)
    hair_color: Column(String)
    skin_color: Column(String)
    eye_color: Column(String)
    birth_year: Column(Integer)
    species = Column(String)
    homeworld = Column(String)
    name = Column(String)

class Planet(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String)
    population = Column(Integer)
    climate = Column(String)
    terrain = Column(String)
    surface_water = Column(Integer)
    name = Column(String)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

# Create an engine to connect to the database
engine = create_engine('sqlite:///starwars.db')

# Create a session to manage the database
Session = sessionmaker(bind=engine)
session = Session()

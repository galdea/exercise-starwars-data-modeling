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
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    species = Column(String)
    homeworld = Column(String)
    gender = Column(String)
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
    url = Column(String)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

# Create an engine to connect to the database
engine = create_engine('sqlite:///starwars.db')

# Create a session to manage the database
Session = sessionmaker(bind=engine)
session = Session()

planet1 = Planet(climate="Arid", diameter=10465, gravity="1", name="Tatooine", orbital_period=304, population=120000, rotation_period=23, surface_water=1, terrain="Dessert", url="https://www.swapi.tech/api/planets/1")
planet2 = Planet(diameter=12240, rotation_period=24, orbital_period=368, gravity="1 standard", population=1000000000000, climate="temperate", terrain="cityscape, mountains", surface_water="unknown", name="Coruscant", url="https://www.swapi.tech/api/planets/9")

session.add(planet1)
session.add(planet2)

character1 = Character(birth_year="19 BBY", eye_color="Blue", gender="Male", hair_color="Blond", height=172, homeworld="https://www.swapi.tech/api/planets/1/", mass=77, name="Luke Skywalker", skin_color="Fair")
character2 = Character(name="Leia Organa", height=150, mass=49, hair_color="brown", skin_color="light", eye_color="brown", birth_year="19BBY", gender="female", homeworld="https://www.swapi.tech/api/planets/2")

session.add(character1)
session.add(character2)

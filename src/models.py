import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    username = Column(String(30), nullable = False, unique = True)
    password = Column(String(30), nullable = False)
    email= Column(String(30), nullable = False, unique = True)

    favourites = relationship('favourites') #Al hacer esta declaracion, estoy diciendo de uno a muchos. Uno siendo "User" y muchos siendo "Favourites"


class Characters(Base):
    __tablename__= "characters"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False) #Nullable significa que es obligatorio
    faction = Column(String(30), nullable = False)
    homeworld = Column(String(30), nullable = False)
    height = Column(Integer, nullable = True)
    hair_color = Column(String(30), nullable = True)
    eye_color = Column(String(15), nullable = True)
    gender = Column(String(15), nullable = True)

    favourites = relationship('favourites')

  
    

class Planets(Base):
    __tablename__= "planets"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    population = Column(Integer, nullable = False)
    climate = Column(String(30), nullable = True)
    terrain = Column(String(30), nullable = True)
    diameter = Column(Integer, nullable = True)
    rotation_period = Column(Integer, nullable = True)
    orbital_period = Column(Integer, nullable = True)
    surface_water = Column(Integer, nullable = True)
    gravity = Column(String(30), nullable = True)

    favourites = relationship('favourites')

    #Relacion con Character para saber de que planeta son los personajes
    characters_id = Column(Integer, ForeignKey('characters.id')) #Aqui se declara la instancia con la que te vas a relacionar
    characters = relationship(Characters) #Aqui se declara con cual tabla se va a relacionar



class Favourites(Base):
    __tablename__ = "favourites"
    id = Column(Integer, primary_key = True)

    characters_id = Column(Integer, ForeignKey('characters.id'), nullable = True) #Al hacer nullable True, el favorito puede o no tener un persona/planeta favorito
    characters = relationship(Characters)

    planets_id = Column(Integer, ForeignKey('planets.id'), nullable = True)
    planets = relationship(Planets)

    #Relacion con Usuario para que pueda marcar favoritos
    user_id = Column(Integer, ForeignKey('user.id'), nullable = False) #Obligatoriamente tiene que tener un favorito. Se necesita un usuario para crear un favorito.
    user = relationship(User)







    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

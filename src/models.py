import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable= False)
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    birth_year = Column(Integer, nullable=False)
    eye_color = Column (String(120), nullable=False)
    hair_color = Column (String(120), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    diameter = Column (String(120), nullable=False)
    climate = Column (String(120), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    
    user = relationship(User)
    planet = relationship(Planet)
    character = relationship(Character)
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

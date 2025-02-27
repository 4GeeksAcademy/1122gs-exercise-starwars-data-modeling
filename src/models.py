import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable = True) #required = True
    password: Mapped[str] = mapped_column(nullable = True) #required = True



class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    user_favorite : Mapped[int] = mapped(ForeignKey("user.id"))
    planet_favorite: Mapped[int] = mapped_column(ForeignKey("planet.id"))
    character_favorite: Mapped[int] = mapped_column(ForeignKey('character.id'))


class Character(Base):
        __tablename__ = 'character'
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(nullable=False)
        height: Mapped[int] = mapped_column(nullable=False)
        eye_color = Mapped[str]
        gender: Mapped[str]


class Planet(Base):
        __tablename__ = 'planet'
        id: Mapped[int] = mapped_column(primary_key=True)
        population: Mapped[str] = mapped_column(nullable=False)
        size: Mapped[str] = mapped_column(nullable=False)
        gas: Mapped[str]

        
    

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

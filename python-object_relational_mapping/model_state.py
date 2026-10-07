#!/usr/bin/python3
"""
Contains State class and Base = declarative_base()
to link to the MySQL table states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Instance de base déclarative requise par SQLAlchemy pour associer les classes aux tables
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base and maps to MySQL table states.
    """
    # Nom exact de la table dans MySQL
    __tablename__ = 'states'

    # Colonne ID : clé primaire auto-incrémentée, unique et non nulle
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True,
        unique=True
    )
    # Colonne Name : chaîne de 128 caractères max, non nulle
    name = Column(String(128), nullable=False)

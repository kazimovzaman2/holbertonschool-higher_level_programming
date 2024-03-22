#!/usr/bin/python3

"""
Filter states by user input
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class City(Base):
    """
    Represents a city in the database.
    """

    __tablename__ = "cities"

    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True,
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

#!/usr/bin/python3

"""
Filter states by user input
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.
    """

    __tablename__ = "states"

    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False,
        autoincrement=True,
    )
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

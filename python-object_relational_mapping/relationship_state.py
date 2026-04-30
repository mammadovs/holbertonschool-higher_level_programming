#!/usr/bin/python3
"""
This module contains the class definition of a State.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class with a relationship to City.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Relationship with City
    # cascade="all, delete" ensures cities are deleted if state is deleted
    # backref="state" creates a .state attribute on City objects
    cities = relationship("City", backref="state", cascade="all, delete")

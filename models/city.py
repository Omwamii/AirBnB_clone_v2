#!/usr/bin/python3
"""
City Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """City class handles all application cities"""

    __tablename__ = "cities"
    __table_args__ = (
            {'mysql_default_charset': 'latin1'})
    if STORAGE_TYPE == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities', cascade='delete')
    else:
        state_id = ''
        name = ''
        places = []

#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import environ as env
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # make rlship with city objects for automatic deletion of linked cities
    cities = relationship('City', cascade='all, delete', backref='state')

    if env.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ getter: return list of City instances
            with state_id same as current id
            """
            obj_dict = models.storage.all(City)
            related = list()
            for key, val in obj_dict.items():
                if val.state_id == self.id:
                    related.append(val)
            return related

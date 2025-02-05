#!/usr/bin/python3
""" Place Module for HBNB project
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
# from sqlalchemy.orm import backref

STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')

place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id')),
        Column('amenity_id', String(60), ForeignKey('amenities.id')),
        mysql_charset="latin1"
        )


class Place(BaseModel, Base):
    """Place class handles all application places"""

    __tablename__ = "places"
    __table_args__ = (
            {'mysql_default_charset': 'latin1'})
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenities = relationship('Amenity', secondary="place_amenity",
                             viewonly=False, backref="place")
    reviews = relationship('Review', backref='place', cascade='delete')

    amenity_ids = []

    if STORAGE_TYPE != "db":
        @property
        def amenities(self):
            """ getter for amenitiess list, i.e. amenities attribute of self
            """
            if len(self.amenity_ids) > 0:
                return self.amenity_ids
            else:
                return None

        @amenities.setter
        def amenities(self, amenity_obj):
            """ setter for amenity_ids
            """
            if amenity_obj and amenity_obj not in self.amenity_ids:
                if amenity_obj.__class__.__name__ == "Amenity":
                    self.amenity_ids.append(amenity_obj.id)

        @property
        def reviews(self):
            """ getter for reviews list, i.e. reviews attribute of self
            """
            if len(self.review_ids) > 0:
                return self.review_ids
            else:
                return None

        @reviews.setter
        def reviews(self, review_obj):
            """ setter for review_ids
            """
            if review_obj and review_obj not in self.review_ids:
                self.review_ids.append(review_obj.id)

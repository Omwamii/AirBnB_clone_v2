#!/usr/bin/python3
""" database storage module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from models.base_model import BaseModel
from os import environ as env


class DBStorage():
    """ DB storage class
    """
    __engine = None
    __session = None
    __clsdict = {
            "State": State,
            "City": City,
            "User": User,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def __init__(self):
        """ initialize variables """
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                    env['HBNB_MYSQL_USER'],
                    env['HBNB_MYSQL_PWD'],
                    env['HBNB_MYSQL_HOST'],
                    env['HBNB_MYSQL_DB']
                    ), pool_pre_ping=True
                )
        if env.get('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)  # drop all tables

    def all(self, cls=None):
        """ query on the current database session (self.__session)
        all objects depending on the class name.
        if cls is None query all types
        """
        d = {}
        cls = cls if not isinstance(cls, str) else self.__clsdict.get(cls)
        if cls:
            for obj in self.__session.query(cls):
                d["{}.{}".format(
                    cls.__name__, obj.id
                    )] = obj
            return (d)
        for k, cls in self.__clsdict.items():
            for obj in self.__session.query(cls):
                d["{}.{}".format(cls.__name__, obj.id)] = obj
        return (d)

    def new(self, obj):
        """ add a new object to the current DB session
        """
        if obj:
            self.__session.add(obj)
            self.save()  # commit changes

    def save(self):
        """ commit all changes to the current db session
        """
        self.__session.commit()  # commit changes made

    def delete(self, obj=None):
        """ delete obj from current session if not None
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ create all tables in db (all classes)
        """
        Base.metadata.create_all(self.__engine)
        Sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Sesh)()

    def close(self):
        """ remove current session and rollback all unsaved trans
        """
        if self.__session:
            self.__session.close()

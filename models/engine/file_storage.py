#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        cls_objs = dict()
        for key, value in self.__objects.items():
            if eval(value.__class__.__name__) == cls:  # potential issue
                cls_objs[key] = value
        return cls_objs

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = dict()
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                for obj in json.load(f).values():
                    # create obj and store in self.__objects
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete obj from __objects if its inside """
        if obj:
            del self.__objects[f'{obj.__class__.__name__}.{obj.id}']
        self.save()

    def close(self):
        """ deserialize JSON file to objects """
        self.reload()

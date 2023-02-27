#!/usr/bin/python3
"""Write a class BaseModel that defines all
common attributes/methods for other classes"""


import uuid
import datetime
from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs["id"]
            self.created_at = kwargs["created_at"]
            self.updated_at = kwargs["updated_at"]
        
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the public instance attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        __dict__ se usa para almacenar los atributos del objeto."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

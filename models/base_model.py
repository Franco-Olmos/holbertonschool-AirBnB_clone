#!/usr/bin/python3
"""Write a class BaseModel that defines all
common attributes/methods for other classes"""


import uuid
import datetime


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()


    def __str__(self):
        """????????????????"""
        return (f."[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the public instance attribute"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        __dict__ se usa para almacenar los atributos del objeto."""
        new_dict = self.__dict__.copy()
        __class__
        .isoformat()
        return new_dict

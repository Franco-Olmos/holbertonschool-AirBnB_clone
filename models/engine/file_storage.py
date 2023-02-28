#!/usr/bin/python3
"""FileStorage"""


import json
from os import path
import os.path


class FileStorage:
    """dddddddddddddddddddd"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(json_dict, f)

    def reload(self):
        from models.base_model import BaseModel
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as f:
            json_dict = json.load(f)

            for key, value in json_dict.items():
                FileStorage.__objects[key] = BaseModel(**value)


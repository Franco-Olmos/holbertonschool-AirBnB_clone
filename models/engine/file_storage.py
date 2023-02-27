#!/usr/bin/python3
"""FileStorage"""
import json
from os import path


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
            f.write(json.dumps(json_dict))

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, encoding="utf-8") as f:
                json_dict = f.read()
                json.loads(json_dict)

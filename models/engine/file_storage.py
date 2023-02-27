#!/usr/bin/python3
""" FileStorage """
import json
from os import path


class FileStorage:
    """ Serialize and Deserialize """

    __file_path = "storage.json"
    __objects = {}

    def all(self):
    """ Returns all saved objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Set in __objects """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ Serialize __objects to JSON """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict.update({key: value.to_dict()})

        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ Deserealize JSON to __objects """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if not path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, mode='r') as f:
            obj_dict = json.load(f)
            classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                       'City': City, 'Amenity': Amenity,
                       'Place': Place, 'Review': Review}
            FileStorage.__objects = {}

            for key, value in obj_dict.items():
                class_name = key.split('.')[0]
                if class_name in classes.keys():
                    FileStorage.__objects[key] = classes[class_name](**value)

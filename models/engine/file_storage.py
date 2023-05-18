#!/usr/bin/python3
"""
FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json
import sys
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        my_string = json.dumps(self.__objects)
        with open(self.__file_path, "w") as file:
            file.write(my_string)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            file = open(self.__file_path, "r")
            my_string = file.read()
            ob = json.loads(my_string)
            for key in ob:
                self.__objects[key] = classes[ob[key]["__class__"]](**ob[key])
            file.close()
        except:
            pass

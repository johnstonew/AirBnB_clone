#!/usr/bin/python3
"""
FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json
import sys
from models.base_model import BaseModel


class FileStorage(BaseModel):
    """
    FileStorage class
    """

    __file_path = "file.json"
    __objects

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects = super().id

    def save(self):
        """
        serializes __objects to the JSON file
        """
        my_string = JSON.dumps(self.__objects)
        with open(self.__file_path, "w") as file:
            file.write(my_string)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            file = open(self.__file_path, "r")
            my_string = file.read()
            self.__objects = JSON.loads(my_string)
        finally:
            file.close()

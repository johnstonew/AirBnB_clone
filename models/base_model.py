#!/usr/bin/python3
"""
Base class for the AIRBNB Shell
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    Base Model Class
    Defines base model to be used with all the classes
    Args
    @created_at: datetime - assign with the
        current datetime when an instance is created
    @updated_at: datetime - assign with the
        current datetime when an instance
        is created and it will be updated
        every time you change your object
    """

    def __init__(self, *args, **kwargs):
        """
        Initial value when method is called
        @name: Name of the instance
        """
        self.my_number = 1
        self.name = ""
        self.updated_at = datetime.today()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        if not isinstance(models.storage, BaseModel):
            models.storage.new(self)

    def __str__(self):
        """
        prints
        [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return f"[{class_name}], ({self.id}), {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

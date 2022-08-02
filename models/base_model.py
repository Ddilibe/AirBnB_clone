#!/usr/bin/python3
"""
    The module containing the base model of the AirBnB Project
"""
from models import storage
from datetime import datetime
import uuid


class BaseModel:
    """
        The base model of the AirBnB project
    """
    def __init__(self, *args, **kwargs):
        """ Public instance method
                id: Unique Id
                created_at: Current datetime when instance is created
                updated_at: datetime when instance is created and updated
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                form = "%Y-%m-%dT%H:%M:%S.%f"
                if key is ("created_at" or "updated_at"):
                    value = datetime.strptime(kwargs[key], form)
                if key != "__class__":
                    setattr(self, key, value)
        
    def __str__(self, name="BaseModel"):
        """ Public instance method to give a description of the class """
        name = self.__class__.__name__
        desc = "[{}] ({}) {}".format(name, self.id, self.__dict__)
        return (desc)

    def save(self):
        """ Public Instance method for updating instance saved parameters """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Public Instance Method that returns a dictionary containing all
        keys and values of a __dict__"""
        new_dictionary = {}
        name = self.__class__.__name__
        for key in self.__dict__.keys():
            if type(self.__dict__[key]) == type(datetime.now()):
                new_dictionary[key] = datetime.isoformat(getattr(self, key))
                continue
            new_dictionary[key] = getattr(self, key)
        new_dictionary["__class__"] = name
        return (new_dictionary)

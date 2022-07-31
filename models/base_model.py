#!/usr/bin/python3
"""
    The module containing the base model of the AirBnB Project
"""
from datetime import datetime
import uuid


class BaseModel:
    """
        The base model of the AirBnB project
    """
    def __init__(self):
        """ Public instance method
                id: Unique Id
                created_at: Current datetime when instance is created
                updated_at: datetime when instance is created and updated
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self, name="BaseModel"):
        """ Public instance method to give a description of the class """
        name = str(self.__class__).split(".")[-1].split('\'>')[0]
        desc = "[{}] ({}) {}".format(name, self.id, self.__dict__)
        return (desc)

    def save(self):
        """ Public Instance method for updating instance saved parameters """
        self.created_at = datetime.now()

    def to_dict(self):
        """ Public Instance Method that returns a dictionary containing all
        keys and values of a __dict__"""
        new_dictionary = {}
        name = str(self.__class__).split(".")[-1].split('\'>')[0]
        for key in self.__dict__.keys():
            if type(self.__dict__[key]) == type(datetime.now()):
                new_dictionary[key] = datetime.isoformat(getattr(self, key))
                continue
            new_dictionary[key] = getattr(self, key)
        new_dictionary["__class__"] = name
        return (new_dictionary)

#!/usr/bin/python3
"""
    Module for the Amentiy class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Amenity class created from the BaseModel class
        Public class attributes:
            @name: The name of the last amenity
    """
    name:str = ""

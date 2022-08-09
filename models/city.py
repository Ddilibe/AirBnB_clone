#!/usr/bin/python3
"""
    Module for building the A new City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        City class made from the BaseModel class
        Public class attribute:
            @state_id: The id of the state in which the city will be
            @name: The name of the city
    """
    name = ""
    state_id = ""

#!/usr/bin/python3
"""
    Module to Build the State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
        State class made from the BaseModel class
        Public class attributes:
            @name: Name of the state
    """
    name:str = ""

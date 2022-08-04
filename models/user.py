#!/usr/bin/python3
"""
    Module which inherits from the base model and creates a user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        User class created from the BaseModel class
        Public class attribute:
            @email: Email Address of the user
            @password: The password of the user
            @first_name: The first name of the user
            @last_name: The last name of the user
    """
    email:str = ""
    password:str = ""
    first_name:str = ""
    last_name:str = ""

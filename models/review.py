#!/usr/bin/python3
"""
    Module used to create the review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Review class created from the BaseModel
        Public class attribute:
            @place_id: The id of the place the review is being made
            @user_id: Id of the user giving the review
            @text: The details of the review from the user
    """
    place_id:str = ""
    user_id:str = ""
    test:str = ""

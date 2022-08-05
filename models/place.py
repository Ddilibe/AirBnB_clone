#!/usr/bin/python3
"""
    Module used for building the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Place class created with the BaseModel
        Public class attributes:
            @city_id: The id of the city it will be created
            @user_id: The id of the user who will create the city
            @name: The name of the place
            @description: The description of the place
            @number_rooms: The number of rooms in the place
            @number_bathrooms: The number of bathrooms in the place
            @max_guest: The maximun number of guests allowed
            @price_by_night: The price of the place at night
            @latitude: The latitudinal location of the place in a map
            @longitude: The longitudinal location of the place in a map
            @amenity_ids: A list of amenity ids
    """
    city_id:str = ""
    user_id = ""
    name:str = ""
    description:str = ""
    number_rooms:int = 0
    number_bathrooms:int = 0
    max_guest:int = 0
    price_by_night:int = 0
    latitude:float = 0.0
    longitude:float = 0.0
    amenity_ids:list = []

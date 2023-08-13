#!/usr/bin/env python3
"""
    This module contains a class called 'Place'
    that inherits from 'BaseModel' """
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Public class attributes:
        city_id: string - empty string, Reference to City.id
        user_id: string - empty string, Reference to User.id
        name: string - empty string, Reference to the name of the place
        description: string - empty string, Reference to the description
        number_rooms: int - empty 0
        number_bathrooms: int - empty 0
        max_guest: int - empty 0
        price_by_night: int - empty 0
        latitude: float - empty 0.0
        longitude: float - empty 0.0
        amenity_ids: list - empty, Reference to a list of Amenity.ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)

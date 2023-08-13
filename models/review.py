#!/usr/bin/env python3
"""
    This module contains a class called 'Review'
    that inherits from 'BaseModel' """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attributes:
        place_id: string - empty string, Reference to Place.id
        user_id: string - empty string, Reference to User.id
        text: string - empty string, Reference to the text of the review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)

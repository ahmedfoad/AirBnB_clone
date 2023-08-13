#!/usr/bin/env python3
"""
    This module contains a class called 'State'
    that inherits from 'BaseModel' """
from models.base_model import BaseModel


class State(BaseModel):
    """
    Public class attributes:
        name: string - empty string, Reference to the name of the state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)

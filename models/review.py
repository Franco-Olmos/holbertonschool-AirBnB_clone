#!/usr/bin/python3
""" shebang """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review Class """
    place_id = ""
    user_id = ""
    text = ""

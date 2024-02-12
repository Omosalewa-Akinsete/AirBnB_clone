#!/usr/bin/python3
"""This module defines the User class that inherits from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

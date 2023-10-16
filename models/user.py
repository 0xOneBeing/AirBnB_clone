#!/usr/bin/python3
"""Defines the User class."""
# Import the BaseModel class from a custom module.
from models.base_model import BaseModel

# Define the User class.
class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    # Initialize attributes for the User class.
    email = ""
    password = ""
    first_name = ""
    last_name = ""


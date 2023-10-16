#!/usr/bin/python3
"""Defines the Amenity class."""
# Import the BaseModel class from a custom module.
from models.base_model import BaseModel

# Define the Amenity class.
class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    # Initialize an empty name attribute for the Amenity.
    name = ""


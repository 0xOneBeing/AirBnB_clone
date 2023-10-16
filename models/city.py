#!/usr/bin/python3
"""Defines the City class."""
# Import the BaseModel class from a custom module.
from models.base_model import BaseModel

# Define the City class.
class City(BaseModel):
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    # Initialize state_id and name attributes for the City.
    state_id = ""
    name = ""


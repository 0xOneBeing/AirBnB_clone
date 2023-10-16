#!/usr/bin/python3
"""Defines the State class."""
# Import the BaseModel class from a custom module.
from models.base_model import BaseModel

# Define the State class.
class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """

    # Initialize the name attribute for the State class.
    name = ""


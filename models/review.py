#!/usr/bin/python3
"""Defines the Review class."""
# Import the BaseModel class from a custom module.
from models.base_model import BaseModel

# Define the Review class.
class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    # Initialize attributes for the Review class.
    place_id = ""
    user_id = ""
    text = ""


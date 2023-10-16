#!/usr/bin/python3
"""Defines the Place class."""
# Import the BaseModel class from a custom module.
from models.base_model import BaseModel

# Define the Place class.
class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """

    # Initialize attributes for the Place class.
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


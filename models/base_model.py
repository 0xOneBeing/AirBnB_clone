#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

# Define the BaseModel class.
class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        # Define the datetime format.
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        
        # Generate a unique ID using uuid4.
        self.id = str(uuid4())
        
        # Set the created_at and updated_at attributes to the current datetime.
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        
        # Check if there are keyword arguments.
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                # If the keyword is 'created_at' or 'updated_at', parse the datetime.
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    # Set other attributes from keyword arguments.
                    self.__dict__[k] = v
        else:
            # If no keyword arguments, add the instance to the storage.
            models.storage.new(self)

    def save(self):
        """Update the updated_at attribute with the current datetime and save to storage."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair __class__ representing the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)


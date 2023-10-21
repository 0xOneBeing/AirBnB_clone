#!/usr/bin/python3
"""Initialization of the storage for models directory"""
# Import the FileStorage class from the engine module.
from models.engine.file_storage import FileStorage

# Create an instance of the FileStorage class for storage.
storage = FileStorage()

# Reload the storage to load existing data if available.
storage.reload()


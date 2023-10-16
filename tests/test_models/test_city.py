#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City

# Define a test case class for testing the instantiation of the City class
class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    # Test whether an instance of City can be created without arguments
    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    # Test whether a new instance of City is stored in the 'objects' attribute of the storage module
    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    # Test the data type of the 'id' attribute of a City instance
    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    # Test the data type of the 'created_at' attribute of a City instance
    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    # Test the data type of the 'updated_at' attribute of a City instance
    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    # Test that 'state_id' is a public class attribute
    def test_state_id_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    # Test that 'name' is a public class attribute
    def test_name_is_public_class_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    # Test that two City instances have unique IDs
    def test_two_cities_unique_ids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    # Test that two City instances have different 'created_at' timestamps
    def test_two_cities_different_created_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    # Test that two City instances have different 'updated_at' timestamps
    def test_two_cities_different_updated_at(self):
        cy1 = City()
        sleep(0.05)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    # Test the string representation of a City instance
    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        cystr = cy.__str__()
        self.assertIn("[City] (123456)", cystr)
        self.assertIn("'id': '123456'", cystr)
        self.assertIn("'created_at': " + dt_repr, cystr)
        self.assertIn("'updated_at': " + dt_repr, cystr)

    # Test that instantiation with None arguments does not add None to the instance's dictionary
    def test_args_unused(self):
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())

    # Test instantiation of a City instance with keyword arguments
    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        cy = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(cy.id, "345")
        self.assertEqual(cy.created_at, dt)
        self.assertEqual(cy.updated_at, dt)

    # Test instantiation of a City instance with None keyword arguments, which should raise a TypeError
    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

# Define a test case class for testing the 'save' method of the City class
class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    # Set up a temporary file for testing
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    # Clean up and restore the original file after testing
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    # Test saving a City instance and checking if 'updated_at' is updated
    def test_one_save(self):
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        self.assertLess(first_updated_at, cy.updated_at)

    # Test saving a City instance twice and checking if 'updated_at' is updated accordingly
    def test_two_saves(self):
        cy = City()
        sleep(0.05)
        first_updated_at = cy.updated_at
        cy.save()
        second_updated_at = cy.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        cy.save()
        self.assertLess(second_updated_at, cy.updated_at)

    # Test saving a City instance with an argument, which should raise a TypeError
    def test_save_with_arg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    # Test that the 'save' method updates the file and adds the City instance's ID
    def test_save_updates_file(self):
        cy = City()
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())

# Define a test case class for testing the 'to_dict' method of the City class
class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    # Test the data type of the output of the 'to_dict' method
    def test_to_dict_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    # Test that the output of 'to_dict' contains the correct keys
    def test_to_dict_contains_correct_keys(self):
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    # Test that the output of 'to_dict' contains added attributes
    def test_to_dict_contains_added_attributes(self):
        cy = City()
        cy.middle_name = "Holberton"
        cy.my_number = 98
        self.assertEqual("Holberton", cy.middle_name)
        self.assertIn("my_number", cy.to_dict())

    # Test that the datetime attributes in the 'to_dict' output are strings
    def test_to_dict_datetime_attributes_are_strs(self):
        cy = City()
        cy_dict = cy.to_dict()
        self.assertEqual(str, type(cy_dict["id"]))
        self.assertEqual(str, type(cy_dict["created_at"]))
        self.assertEqual(str, type(cy_dict["updated_at"]))

    # Test the content of the 'to_dict' output against a predefined dictionary
    def test_to_dict_output(self):
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    # Test that the output of 'to_dict' is different from the instance's '__dict__'
    def test_contrast_to_dict_dunder_dict(self):
        cy = City()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)

    # Test 'to_dict' method with an argument, which should raise a TypeError
    def test_to_dict_with_arg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)

if __name__ == "__main__":
    unittest.main()


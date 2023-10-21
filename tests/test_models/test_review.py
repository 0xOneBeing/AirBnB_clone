#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review

# Define a test case class for testing the instantiation of the Review class
class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    # Test whether an instance of Review can be created without arguments
    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    # Test whether a new instance of Review is stored in the 'objects' attribute of the storage module
    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    # Test the data type of the 'id' attribute of a Review instance
    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id)

    # Test the data type of the 'created_at' attribute of a Review instance
    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    # Test the data type of the 'updated_at' attribute of a Review instance
    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    # Test whether 'place_id' is a public class attribute of the Review class
    def test_place_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)

    # Test whether 'user_id' is a public class attribute of the Review class
    def test_user_id_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict())

    # Test whether 'text' is a public class attribute of the Review class
    def test_text_is_public_class_attribute(self):
        rv = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict())

    # Test that two Review instances have unique IDs
    def test_two_reviews_unique_ids(self):
        rv1 = Review()
        rv2 = Review()
        self.assertNotEqual(rv1.id, rv2.id)

    # Test that two Review instances have different 'created_at' timestamps
    def test_two_reviews_different_created_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.created_at, rv2.created_at)

    # Test that two Review instances have different 'updated_at' timestamps
    def test_two_reviews_different_updated_at(self):
        rv1 = Review()
        sleep(0.05)
        rv2 = Review()
        self.assertLess(rv1.updated_at, rv2.updated_at)

    # Test the string representation of a Review instance
    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        rv = Review()
        rv.id = "123456"
        rv.created_at = rv.updated_at = dt
        rvstr = rv.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    # Test that instantiation with None arguments does not add None to the instance's dictionary
    def test_args_unused(self):
        rv = Review(None)
        self.assertNotIn(None, rv.__dict__.values())

    # Test instantiation of a Review instance with keyword arguments
    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        rv = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(rv.id, "345")
        self.assertEqual(rv.created_at, dt)
        self.assertEqual(rv.updated_at, dt)

    # Test instantiation of a Review instance with None keyword arguments, which should raise a TypeError
    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

# Define a test case class for testing the 'save' method of the Review class
class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

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

    # Test saving a Review instance and checking if 'updated_at' is updated
    def test_one_save(self):
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        self.assertLess(first_updated_at, rv.updated_at)

    # Test saving a Review instance twice and checking if 'updated_at' is updated accordingly
    def test_two_saves(self):
        rv = Review()
        sleep(0.05)
        first_updated_at = rv.updated_at
        rv.save()
        second_updated_at = rv.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rv.save()
        self.assertLess(second_updated_at, rv.updated_at)

    # Test saving a Review instance with an argument, which should raise a TypeError
    def test_save_with_arg(self):
        rv = Review()
        with self.assertRaises(TypeError):
            rv.save(None)

    # Test that the 'save' method updates the 'file.json' file with the Review instance
    def test_save_updates_file(self):
        rv = Review()
        rv.save()
        rvid = "Review." + rv.id
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())

# Define a test case class for testing the 'to_dict' method of the Review class
class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    # Test the data type of the dictionary returned by 'to_dict'
    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    # Test if the dictionary returned by 'to_dict' contains the expected keys
    def test_to_dict_contains_correct_keys(self):
        rv = Review()
        self.assertIn("id", rv.to_dict())
        self.assertIn("created_at", rv.to_dict())
        self.assertIn("updated_at", rv.to_dict())
        self


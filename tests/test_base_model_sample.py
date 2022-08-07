#!/usr/bin/python3
"""
    Module for testing the base model
"""
from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime
from time import sleep

class BaseModelTest(TestCase):
    """
        BaseModel class test created with the TestCase class
    """
    def setUp(self):
        """ Method to setup the test """
        self.first = BaseModel()
        self.second = BaseModel()
        self.third = BaseModel()

    def test_uuid_is_a_string(self):
        """ Method to test that the id is a string """
        self.assertEqual(str, type(self.first.id))
        self.assertEqual(str, type(self.second.id))
        self.assertEqual(str, type(self.third.id))

    def test_created_at_is_type_datetime(self):
        """ Method to test that the created_at is a datetime datatype """
        self.assertEqual(type(datetime.now()), type(self.first.created_at))
        self.assertEqual(type(datetime.now()), type(self.second.created_at))
        self.assertEqual(type(datetime.now()), type(self.third.created_at))

    def test_updated_at_is_type_datetime(self):
        """ Method to test that the updated_at is a datetime datatype """
        self.assertEqual(type(datetime.now()), type(self.first.updated_at))
        self.assertEqual(type(datetime.now()), type(self.second.updated_at))
        self.assertEqual(type(datetime.now()), type(self.third.updated_at))

    def test_save_to_database(self):
        """ Method to test the save """
        self.first.save()
        self.second.save()
        self.third.save()

    def test_time_difference(self):
        """ Method to test that the time difference between the created at and the updated at is equal"""
        self.assertEqual(self.first.updated_at, self.first.created_at)
        self.assertEqual(self.second.updated_at, self.second.created_at)
        self.assertEqual(self.third.updated_at, self.third.created_at)

    def test_after_save(self):
        """ Method to test that the time difference between the created_at and the updated_at is not equal """
        sleep(0.1)
        self.first.save()
        self.second.save()
        self.third.save()
        self.assertNotEqual(self.first.updated_at, self.first.created_at)
        self.assertNotEqual(self.second.updated_at, self.second.created_at)
        self.assertNotEqual(self.third.updated_at, self.third.created_at)

    def test_confirm_to_dict(self):
        """ Method to confirm the to dictionary function """
        self.assertTrue(self.first.to_dict())
        self.assertTrue(self.second.to_dict())
        self.assertTrue(self.third.to_dict())

    def test_confirming_elements_in_the_datetime_for_first(self):
        """ Method to confirm the type of datetime attributes for first"""
        self.assertEqual(str, type(self.first.to_dict()['created_at']))
        self.assertEqual(str, type(self.first.to_dict()['updated_at']))
        self.assertNotEqual(type(datetime.now), type(self.first.to_dict()['created_at']))
        self.assertNotEqual(type(datetime.now), type(self.first.to_dict()['updated_at']))

    def test_confirming_elements_in_the_datetime_for_second(self):
        """ Method to confirm the type of datetime attributes for second """
        self.assertEqual(str, type(self.second.to_dict()['created_at']))
        self.assertEqual(str, type(self.second.to_dict()['updated_at']))
        self.assertNotEqual(type(datetime.now), type(self.second.to_dict()['created_at']))
        self.assertNotEqual(type(datetime.now), type(self.second.to_dict()['updated_at']))

    def test_confirming_elements_in_the_datetime_for_third(self):
        """ Method to confirm the type of datetime attributes for third """
        self.assertEqual(str, type(self.third.to_dict()['created_at']))
        self.assertEqual(str, type(self.third.to_dict()['updated_at']))
        self.assertNotEqual(type(datetime.now), type(self.third.to_dict()['created_at']))
        self.assertNotEqual(type(datetime.now), type(self.third.to_dict()['updated_at']))

    def test_first_dictionary_attributes(self):
        """ Method to test the dictionary attributes of first """
        first = self.first.to_dict()
        self.assertEqual(str, type(first['__class__']))
        self.assertEqual(str, type(first['id']))

    def test_second_dictionary_attributes(self):
        """ Method to test the dictionary attributes of second """
        first = self.second.to_dict()
        self.assertEqual(str, type(first['__class__']))
        self.assertEqual(str, type(first['id']))

    def test_third_dictionary_attributes(self):
        """ Method to test the dictionary attributes of third """
        first = self.third.to_dict()
        self.assertEqual(str, type(first['__class__']))
        self.assertEqual(str, type(first['id']))

    def test_first_dictionary_added_attributes(self):
        """ Method to test the added attributes of a dictionary """
        self.first.age = 43
        self.first.money = 33.45
        first = self.first.to_dict()
        self.assertEqual(int, type(first['age']))
        self.assertEqual(float, type(first['money']))

    def test_second_dictionary_added_attributes(self):
        """ Method to test the added attributes of a dictionary """
        self.second.age = [4, 3]
        self.second.money = {33:45}
        first = self.second.to_dict()
        self.assertEqual(list, type(first['age']))
        self.assertEqual(dict, type(first['money']))

    def test_third_dictionary_added_attributes(self):
        """ Method to test the added attributes of a dictionary """
        self.third.age = (4,3)
        self.third.money = {33,45}
        first = self.third.to_dict()
        self.assertEqual(tuple, type(first['age']))
        self.assertEqual(set, type(first['money']))

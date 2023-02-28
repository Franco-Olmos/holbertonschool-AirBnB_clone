#!/usr/bin/python3
""" UnitTest basemodel """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        with open("file.json", "w") as f:
            FileStorage.__file_path = 'file.json'
            FileStorage.__objects = {}

    def test_save(self):
        with self.assertRaises(AttributeError):
            BaseModel.save(["Hello, World"])
            BaseModel.save([111, 111, 111, 111])

    def test_to_dict(self):
        diccionary = BaseModel()
        dict = diccionary.to_dict()
        self.assertEqual(dict['id'], diccionary.id)
        self.assertEqual(dict['created_at'], diccionary.created_at.isoformat())
        self.assertEqual(dict['updated_at'], diccionary.updated_at.isoformat())
        self.assertEqual(dict['__class__'], 'BaseModel')

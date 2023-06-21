#!/usr/bin/python3
"""Defines unittest for database"""
import pep8
import unittest
import models
import MySQLdb
import os
from models.base_model import Base
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestDBStorage(unittest.TestCase):
    """Unittests for testing the database storage class"""

    @classmethod
    def set_up(self):
        """Testing db setup"""
        if type(models.storage) == DBStorage:
            self.storage

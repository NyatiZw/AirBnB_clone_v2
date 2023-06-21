#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
import pep8
import json
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @classmethod
    def setUpClass(cls):
        """Testing FileStorage setup"""
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        cls.storage = FileStorage()
        cls.base = BaseModel()
        key = "{}.{}".format(type(cls.base).__name__, cls.base.id)
        FileStorage._FileStorage__objects[key] = cls.base
        cls.user = User()
        key = "{}.{}".format(type(cls.user).__name__, cls.user.id)
        FileStorage._FileStorage__objects[key] = cls.user
        cls.state = State()
        key = "{}.{}".format(type(cls.state).__name__, cls.state.id)
        FileStorage._FileStorage__objects[key] = cls.state
        cls.place = Place()
        key = "{}.{}".format(type(cls.place).__name__, cls.place.id)
        FileStorage._FileStorage__objects[key] = cls.place
        cls.city = City()
        key = "{}.{}".format(type(cls.city).__name__, cls.city.id)
        FileStorage._FileStorage__objects[key] = cls.city
        cls.amenity = Amenity()
        key = "{}.{}".format(type(cls.amenity).__name__, cls.amenity.id)
        FileStorage._FileStorage__objects[key] = cls.amenity
        cls.review = Review()
        key = "{}.{}".format(type(cls.review).__name__, cls.review.id)
        FileStorage._FileStorage__objects[key] = cls.review

    @classmethod
    def tearDown(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        del cls.storage
        del cls.base
        del cls.review
        del cls.city
        del cls.amenity
        del cls.user
        del cls.place
        del cls.state

    def test_pep8_FileStorage(self):
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring(self):
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.delete.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_methods(self):
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "delete"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_init(self):
        self.assertTrue(isinstance(self.storage, FileStorage))

    def test_attr(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage,_FileStorage__objects))

    def test_all(self):
        obj = self.storage.all()
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, FileStorage,_FileStorage__objects)
        self.assertEqual(len(obj), 9)

    def test_all_cls(self):
        obj = self.storage.all(BaseModel)
        self.assertEqual(type(obj), dict)
        self.assertEqual(len(obj), 3)
        self.assertEqual(self.base, list(obj.values())[0])

    def test_new(self):
        bm = BaseModel()
        self.storage.new(bm)
        store = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, store.keys())
        self.assertIn(self.base, store.values())

    def test_save(self):
        self.storage.save()
        with open("file.json", "r", encoding="utf-8") as file:
            save_text = file.read()
            self.assertIn("BaseModel." + self.base.id, save_text)
            self.assertIn("User." + self.user.id, save_text)
            self.assertIn("Place." + self.place.id, save_text)
            self.assertIn("City." + self.city.id, save_text)
            self.assertIn("State." + self.state.id, save_text)
            self.assertIn("Review." + self.review.id, save_text)
            self.assertIn("Amenity." + self.amenity.id, save_text)

    def test_reload(self):
        bm = BaseModel()
        with open("file.json", "w", encoding="utf-8") as file:
            k = "{}.{}".format(type(bm).__name__, bm.id)
            json.dump({k: bm.to_dict()}, file)
        self.storage.reload()
        store = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, store)

    def test_del(self):
        bm = BaseModel()
        k = "{}.{}".format(type(bm).__name__, bm.id)
        FileStorage._FileStorage__objects[k] = bm
        self.storage.delete(bm)
        self.assertNotIn(bm, FileStorage,_FileStorage__objects)

    def test_del_none(self):
        try:
            self.storage.delete(BaseModel())
        except Exception:
            self.fail


if __name__ == "__main__":
    unittest.main()

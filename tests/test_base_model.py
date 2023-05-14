import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """
        Test that instance variables are initialized correctly
        """
        model = BaseModel()
        model.name = "test"
        model.my_number = 123
        self.assertEqual(model.name, "test")
        self.assertEqual(model.my_number, 123)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertIsInstance(model.id, str)

    def test_str(self):
        """
        Test that __str__ returns the correct string
        """
        model = BaseModel()
        model_str = str(model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn("id", model_str)
        self.assertIn("created_at", model_str)
        self.assertIn("updated_at", model_str)

    def test_save(self):
        """
        Test that save updates the updated_at attribute
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """
        Test that to_dict returns the correct dictionary
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIn('id', model_dict)


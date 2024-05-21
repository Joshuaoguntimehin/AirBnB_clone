import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test cases"""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if the instance is correctly created"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method"""
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected)

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertTrue(self.model.updated_at > old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())

    def test_kwargs_initialization(self):
        """Test instance initialization with kwargs"""
        model_data = {
            'id': '123',
            'created_at': '2023-01-01T00:00:00.000000',
            'updated_at': '2023-01-01T00:00:00.000000',
            'name': 'Test Model'
        }
        model = BaseModel(**model_data)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.created_at, datetime.strptime('2023-01-01T00:00:00.000000', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(model.updated_at, datetime.strptime('2023-01-01T00:00:00.000000', '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(model.name, 'Test Model')

if __name__ == "__main__":
    unittest.main()

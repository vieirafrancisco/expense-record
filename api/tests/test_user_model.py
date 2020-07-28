import unittest
from unittest.mock import Mock, patch

from db.models import User
from exceptions.db_exceptions import ModelInstanceAlreadyExist

class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.user = User("test_nome", "test_email", 2.5)

    @patch('db.models.db')
    def test_user_model_save_method_return_none(self, db_mock):
        db_mock.insert_into_table.return_value = None
        assert self.user.save() is None

    @patch('db.models.db')
    def test_user_model_save_method_raise_model_instance_already_exist_exception(self, db_mock):
        db_mock.insert_into_table.side_effect = ModelInstanceAlreadyExist
        self.assertRaises(ModelInstanceAlreadyExist, self.user.save)
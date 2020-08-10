import unittest
from unittest.mock import Mock, patch

from src.routes import app

class TestUserCrud(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def tearDown(self):
        pass

    @patch('src.routes.User')
    def test_create_user_return_status_code_200_ok(self, user_mock):
        user_mock.save.return_value = None
        body = {
            "name": "name_test",
            "email": "name_test@mail.com",
            "income": 2.0
        }
        response = self.app.post('/create/user', json=body)
        assert response.status_code == 200

    def test_create_user_return_status_code_400_bad_request(self):
        body = {
            "email": "name_test@mail.com",
            "income": 2.0
        }
        response = self.app.post('/create/user', json=body)
        assert response.status_code == 400

    @patch('src.routes.User')
    def test_create_user_return_status_code_200_ok_with_body_with_more_attributes_than_needed(self, user_mock):
        user_mock.save.return_value = None
        body = {
            "name": "name_test",
            "email": "name_test@mail.com",
            "income": 2.0,
            "ksdjfk": "jkfkldsjf"
        }
        response = self.app.post('/create/user', json=body)
        assert response.status_code == 200

    @patch('src.routes.User')
    def test_create_user_return_status_code_409_conflict_when_user_already_exist(self, user_mock):
        user_mock.side_effect = Exception
        body = {
            "name": "name_test",
            "email": "name_test@mail.com",
            "income": 2.0
        }
        response = self.app.post('/create/user', json=body)
        assert response.status_code == 409

    @patch('src.routes.User')
    def test_get_user_by_email_return_200_ok(self, user_mock):
        email = "test@mail.com"
        user_mock.get_one.return_value = {
            "name": "test_name",
            "email": "test_email",
            "income": 2.5
        }
        response = self.app.get(f'/user/{email}')
        assert response.status_code == 200

    @patch('src.routes.User')
    def test_get_user_by_email_return_user_dictionary(self, user_mock):
        email = "test@mail.com"
        user_mock.get_one.return_value = {
            "name": "test_name",
            "email": "test_email",
            "income": 2.5
        }
        response = self.app.get(f'/user/{email}')
        result_keys = ["name", "email", "income"]
        keys = response.json.keys()
        assert all(map(lambda x: x in keys, result_keys))

    def test_get_user_by_email_when_email_not_exist(self):
        email = "fsdifkjlsdahflk"
        response = self.app.get(f'/user/{email}')
        assert response.status_code == 400
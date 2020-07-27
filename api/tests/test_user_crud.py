import unittest
from unittest.mock import Mock, patch

from src.routes import app

class TestUserCrud(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def tearDown(self):
        pass

    def test_create_user_return_status_code_200_ok(self):
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

    def test_create_user_return_status_code_200_ok_with_body_with_more_attributes_than_needed(self):
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
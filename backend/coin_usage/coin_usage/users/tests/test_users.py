"""Users tests."""
from cerberus import Validator
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from coin_usage.users.models import User

from .users_schemas import user_login_schema, user_schema


class UsersTestCase(TestCase):
    """Users tests."""

    def setUp(self):
        """Set up."""
        self.api = APIClient()
        self.validator = Validator()
        self.headers = {}

    def test_users_signup(self):
        """Test users signup."""
        data = {
            "username": "someusername",
            "email": "some@email.test",
            "password": "Test1234strong*",
            "password_confirmation": "Test1234strong*",
        }
        response = self.api.post("/users/signup/", format="json", data=data)
        is_valid = self.validator.validate(response.data, user_schema)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(is_valid)
        self.assertEqual(response.data["username"], data["username"], User.objects.first().username)

    def test_users_signup_error(self):
        """Test if user signup fail."""
        data = {
            "username": "someusername",
            "email": "some@email.test",
            "password": "Test",
            "password_confirmation": "Test",
        }
        response = self.api.post("/users/signup/", format="json", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_users_login(self):
        """Test users login."""
        data = {
            "username": "someusername",
            "password": "Test1234strong*",
        }
        self._create_user()
        response = self.api.post("/users/login/", format="json", data=data)
        is_valid = self.validator.validate(response.data, user_login_schema)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(is_valid)

    def test_users_login_error(self):
        """Test if user login fail."""
        data = {
            "username": "someusername",
            "password": "test1234",
        }
        self._create_user()
        response = self.api.post("/users/login/", format="json", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def _create_user(self):
        """Create user."""
        data = {
            "username": "someusername",
            "email": "some@email.test",
            "password": "Test1234strong*",
            "password_confirmation": "Test1234strong*",
        }
        self.api.post("/users/signup/", format="json", data=data)

"""Tests utilities."""
from cerberus import Validator
from rest_framework.test import APIClient

from coin_usage.users.models import User


class TestUtils:
    """Test utilities."""

    def initialize(self):
        """Initialize."""
        self.api = APIClient()
        self.validator = Validator()
        self.headers = {}
        self.user_data = {
            "username": "someusername",
            "email": "some@email.test",
            "password": "Test1234strong*",
            "password_confirmation": "Test1234strong*",
        }
        self.coin_data = {"ticker_symbol": "RPC", "name": "Ripio Coin"}

    def create_user(self):
        """Create user."""
        self.initialize()
        self.api.post("/users/signup/", format="json", data=self.user_data)

    def create_superuser(self):
        """Create superuser."""
        self.initialize()
        self.user_data.pop("password_confirmation")
        self.user_data["is_staff"] = True
        return User.objects.create_superuser(**self.user_data)

    def login_user(self):
        """Login user."""
        self.initialize()
        self.create_user()
        data = {
            "username": self.user_data["username"],
            "password": self.user_data["password"],
        }
        response = self.api.post("/users/login/", format="json", data=data)
        return response.json()

    def login_superuser(self):
        """Login superuser."""
        self.initialize()
        self.create_superuser()
        data = {
            "username": self.user_data["username"],
            "password": self.user_data["password"],
        }
        response = self.api.post("/users/login/", format="json", data=data)
        return response.json()

    def create_coin(self):
        """Create coin."""
        access_token = self.login_superuser()["access_token"]
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        self.api.post("/coins/", format="json", data=self.coin_data)

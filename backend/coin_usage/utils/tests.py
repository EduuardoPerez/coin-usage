"""Tests utilities."""
from rest_framework.test import APIClient

api = APIClient()
user_data = {
    "username": "someusername",
    "email": "some@email.test",
    "password": "Test1234strong*",
    "password_confirmation": "Test1234strong*",
}


def create_user():
    """Create user."""
    api.post("/users/signup/", format="json", data=user_data)


def login_user():
    """Login user."""
    create_user()
    data = {
        "username": user_data["username"],
        "password": user_data["password"],
    }
    api.post("/users/login/", format="json", data=data)

"""Coins tests."""
from django.test import TestCase
from rest_framework import status

from coin_usage.coins.models import Coin
from coin_usage.utils.tests import TestUtils

from .schemas.coins_schemas import coin_schema


class CoinsTestCase(TestCase, TestUtils):
    """Coins tests."""

    def setUp(self):
        """Set up."""
        self.initialize()

    def test_create_coin(self):
        """Test create a coin."""
        access_token = self.login_superuser()["access_token"]
        breakpoint()
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        response = self.api.post("/coins/", format="json", data=self.coin_data)
        is_valid = self.validator.validate(response.data, coin_schema)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertTrue(is_valid)
        self.assertEqual(
            response.data["ticker_symbol"], self.coin_data["ticker_symbol"], Coin.objects.first().ticker_symbol
        )

    def test_create_coin_not_superuser_error(self):
        """Test if a normal user cannot create a coin."""
        access_token = self.login_user()["access_token"]
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        response = self.api.post("/coins/", format="json", data=self.coin_data)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_create_coin_duplicate_ticker_symbol_error(self):
        """Test a coin cannot be created with same ticker symbol."""
        Coin.objects.create(**self.coin_data)
        access_token = self.login_superuser()["access_token"]
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        response = self.api.post("/coins/", format="json", data=self.coin_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

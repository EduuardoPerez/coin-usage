"""Accounts tests."""
from django.test import TestCase
from rest_framework import status

from coin_usage.accounts.models import Account, Balance
from coin_usage.coins.models import Coin
from coin_usage.users.models import User
from coin_usage.utils.tests import TestUtils

from .schemas.accounts_schemas import account_balance_schema


class AccountTestCase(TestCase, TestUtils):
    """Accounts tests."""

    def setUp(self):
        """Set up."""
        self.initialize()

    def test_deposit_in_new_account_balance(self):
        """Check if a deposit can be made."""
        self.create_coin()
        access_token = self.login_user()["access_token"]
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        data = {"balance": {"coin": "RPC", "amount": 100}}
        response = self.api.patch("/accounts/deposit/", data=data, format="json")
        is_valid = self.validator.validate(response.data, account_balance_schema)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(is_valid)
        self.assertEqual(
            response.json()["balances"][0]["coin"], data["balance"]["coin"], Balance.objects.first().coin.ticker_symbol
        )
        self.assertEqual(
            response.json()["balances"][0]["amount"], data["balance"]["amount"], Balance.objects.first().amount
        )

    def test_deposit_in_account_with_balance(self):
        """Test in account with balance."""
        self.create_coin()
        coin = Coin.objects.first()
        Balance.objects.create(coin=coin, account=User.objects.first().account, amount=50)
        access_token = self.login_user()["access_token"]
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        data = {"balance": {"coin": coin.ticker_symbol, "amount": 100}}
        response = self.api.patch("/accounts/deposit/", data=data, format="json")
        is_valid = self.validator.validate(response.data, account_balance_schema)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(is_valid)
        self.assertEqual(response.json()["balances"][0]["amount"], Balance.objects.first().amount, 150)

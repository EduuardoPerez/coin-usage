"""Accounts tests."""
from django.test import TestCase
from model_bakery import baker
from rest_framework import status

from coin_usage.accounts.models import Balance
from coin_usage.coins.models import Coin
from coin_usage.users.models import User
from coin_usage.utils.tests import TestUtils

from .schemas.accounts_schemas import account_balance_schema, balance_schema


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

    def test_send_coin_to_another_user_with_balance_in_coin(self):
        """Test in account with balance."""
        self.create_coin()
        coin = Coin.objects.first()
        another_user = User.objects.create_user(
            username="another_user",
            email="another@user.test",
            password="anotherTest1234strong*",
        )
        Balance.objects.create(coin=coin, account=User.objects.first().account, amount=50)
        Balance.objects.create(coin=coin, account=another_user.account, amount=75)
        access_token = self.login_user()["access_token"]
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        data = {
            "address": another_user.account.address,
            "balance": {
                "coin": coin.ticker_symbol,
                "amount": 25,
            },
        }
        response = self.api.patch("/accounts/send/", data=data, format="json")
        is_valid = self.validator.validate(response.data, account_balance_schema)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(is_valid)
        self.assertEqual(
            response.json()["balances"][0]["amount"],
            Balance.objects.get(account__address=response.json()["address"], coin=coin).amount,
            25,
        )

    def test_send_coin_to_another_user_without_balance_in_coin(self):
        """Test in account without balance."""
        self.create_coin()
        coin = Coin.objects.first()
        another_user = User.objects.create_user(
            username="another_user",
            email="another@user.test",
            password="anotherTest1234strong*",
        )
        Balance.objects.create(coin=coin, account=User.objects.first().account, amount=50)
        access_token = self.login_user()["access_token"]
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        data = {
            "address": another_user.account.address,
            "balance": {
                "coin": coin.ticker_symbol,
                "amount": 25,
            },
        }
        response = self.api.patch("/accounts/send/", data=data, format="json")
        is_valid = self.validator.validate(response.data, account_balance_schema)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(is_valid)
        self.assertEqual(
            response.json()["balances"][0]["amount"],
            Balance.objects.get(account__address=response.json()["address"], coin=coin).amount,
            25,
        )
        self.assertEqual(another_user.account.balances.first().amount, 25)

    def test_balances_account(self):
        """Check the balances of an account."""
        self.create_coin()
        coin = Coin.objects.first()
        Balance.objects.create(coin=coin, account=User.objects.first().account, amount=50)
        access_token = self.login_user()["access_token"]
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        response = self.api.get("/accounts/balances/", format="json")
        is_valid = self.validator.validate(response.data, account_balance_schema)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(is_valid)
        self.assertEqual(response.json()["balances"][0]["amount"], Balance.objects.first().amount, 50)

    def test_balances_coin_account(self):
        """Check the balances of a coin in an account."""
        ticker_symbol = self.create_coin()
        account = User.objects.first().account
        baker.make("accounts.Balance", account=account, _quantity=3)
        coin = Coin.objects.get(ticker_symbol=ticker_symbol)
        balance = Balance.objects.create(coin=coin, account=account, amount=50)
        access_token = self.login_user()["access_token"]
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        response = self.api.get(f"/accounts/coins/?coin={ticker_symbol}", format="json")
        is_valid = self.validator.validate(response.data, balance_schema)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(is_valid)
        self.assertEqual(response.json()["amount"], balance.amount, 50)

    def test_balances_coin_account_error(self):
        """Check the balances of a coin in an account."""
        access_token = self.login_user()["access_token"]
        account = User.objects.first().account
        baker.make("accounts.Balance", account=account, _quantity=3)
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        response = self.api.get("/accounts/coins/", format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

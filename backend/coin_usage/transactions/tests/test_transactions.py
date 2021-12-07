"""Transactions tests."""
from django.test import TestCase
from model_bakery import baker
from rest_framework import status

from coin_usage.accounts.models import Balance
from coin_usage.coins.models import Coin
from coin_usage.transactions.models import Transaction
from coin_usage.users.models import User
from coin_usage.utils.tests import TestUtils


class TransactionTestCase(TestCase, TestUtils):
    """Transaction tests."""

    def setUp(self):
        """Set up."""
        self.initialize()

    def test_list_transactions(self):
        """Test list transactions."""
        baker.make("transactions.Transaction", _quantity=5)
        response = self.api.get("/transactions/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 5)

    def test_transaction_register(self):
        """Test register transaction."""
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
        self.api.patch("/accounts/send/", data=data, format="json")
        self.assertEqual(Transaction.objects.count(), 1)
        transaction = Transaction.objects.first()
        self.assertEqual(transaction.account_to, another_user.account)

"""Transactions tests."""
from django.test import TestCase
from model_bakery import baker
from rest_framework import status

from coin_usage.utils.tests import TestUtils


class TransactionTestCase(TestCase, TestUtils):
    """Transaction tests."""

    def setUp(self):
        """Set up."""
        self.initialize()

    def test_list_balances(self):
        """Test list transactions."""
        baker.make("accounts.Balance", _quantity=5)
        access_token = self.login_superuser()["access_token"]
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        response = self.api.get("/balances/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 5)

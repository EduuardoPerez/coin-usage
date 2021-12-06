"""Accounts tests."""
from django.test import TestCase
from rest_framework import status

from coin_usage.utils.tests import TestUtils


class AccountTestCase(TestCase, TestUtils):
    """Accounts tests."""

    def setUp(self):
        """Set up."""
        self.initialize()

    def test_deposit_in_new_account(self):
        """Test deposit."""
        access_token = self.login_user()["access_token"]
        self.api.credentials(HTTP_AUTHORIZATION=f"Token {access_token}")
        data = {"coin": "RPC", "amount": 100}
        response = self.api.patch("/accounts/deposit/", data=data, format="json")
        breakpoint()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["amount"], 100)
        self.assertEqual(response.data["balance"], 100)

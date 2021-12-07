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
        baker.make("transactions.Transaction", _quantity=5)

    def test_list_transactions(self):
        """Test list transactions."""
        response = self.api.get("/transactions/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 5)

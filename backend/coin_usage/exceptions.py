"""Custom exceptions for coin_usage."""
from django.utils.translation import gettext_lazy as _


class InsufficientFunds(Exception):
    """Exception raised when a user tries to spend more than they have."""

    def __init__(self, message=_("Insufficient funds")):
        """Initialize the exception."""
        self.message = message


class InvalidAmount(Exception):
    """Exception raised when a user tries to use an invalid amount."""

    def __init__(self, message=_("Invalid amount")):
        """Initialize the exception."""
        self.message = message

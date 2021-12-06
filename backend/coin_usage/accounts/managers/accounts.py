"""Accounts manager."""
from django.db import models
from django.utils.crypto import get_random_string


class AccountsManager(models.Manager):
    """Accounts manager.

    Used to handle code address creation.
    """

    ADDRESS_LENGTH = 35

    def create(self, **kwargs):
        """Create a new account."""
        kwargs["address"] = self._generate_address()
        return super(AccountsManager, self).create(**kwargs)

    def _generate_address(self):
        """Generate a new address for the account."""
        address = get_random_string(length=self.ADDRESS_LENGTH)
        while self.filter(address=address).exists():
            address = get_random_string(length=35)
        return get_random_string(length=35)

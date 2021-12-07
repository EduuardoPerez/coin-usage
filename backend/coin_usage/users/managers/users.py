"""Users manager."""
from django.contrib.auth.models import UserManager

from coin_usage.accounts.models import Account


class UsersManager(UserManager):
    """Users manager.

    Used to handle code address creation.
    """

    def create(self, **kwargs):
        """Create a new user with its account."""
        user = super(UsersManager, self).create(**kwargs)
        user.account = Account.objects.create(user=user)
        user.save()
        return user

    def create_user(self, username, email, password, **extra_fields):
        """Create a new user with its account."""
        user = super().create_user(username, email=email, password=password, **extra_fields)
        user.account = Account.objects.create(user=user)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """Create a new superuser with its account."""
        user = super().create_superuser(username, email, password, **extra_fields)
        user.account = Account.objects.create(user=user)
        user.save()
        return user

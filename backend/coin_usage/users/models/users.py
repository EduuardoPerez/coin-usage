"""User model."""
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.utils.translation import gettext_lazy as _

from coin_usage.users.managers import UsersManager


class User(AbstractUser):
    """User model.

    Extend from Django's Abstract User and add some extra fields.
    """

    email = EmailField(
        "email address", unique=True, error_messages={"unique": _("A user with that email already exists.")}
    )
    first_name = CharField(_("First name of user"), blank=True, null=True, max_length=30)
    last_name = CharField(_("Last name of user"), blank=True, null=True, max_length=30)

    objects = UsersManager()

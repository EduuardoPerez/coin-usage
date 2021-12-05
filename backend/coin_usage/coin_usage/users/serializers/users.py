"""Users serializers."""
from django.contrib.auth import authenticate, password_validation
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from coin_usage.users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""

        model = User
        fields = ("email", "username", "first_name", "last_name")


class UserSignUpSerializer(serializers.Serializer):
    """User sign up serializer.

    Handle sign up data validation and user creation.
    """

    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
        min_length=4, max_length=20, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)
    first_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=30, required=False, allow_blank=True)

    def validate(self, data):
        """Verify passwords match."""
        password = data["password"]
        password_conf = data["password_confirmation"]
        if password != password_conf:
            raise serializers.ValidationError(_("Passwords don't match."))
        password_validation.validate_password(password)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop("password_confirmation")
        user = User.objects.create_user(**data)
        return user


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.

    Handle the login request data.
    """

    username = serializers.CharField(min_length=4, max_length=20)
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials."""
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError(_("Invalid credentials"))
        self.context["user"] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""
        token, created = Token.objects.get_or_create(user=self.context["user"])
        return self.context["user"], token.key

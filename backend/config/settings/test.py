"""With these settings, tests run faster."""

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="OmkGcfPFGXw3DA5bdGlgQrY68ttDYQOLvjCcL4oQ8jYtKU29qML43lG8aqyZdYIZ",
)
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# PASSWORDS
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[-1]["OPTIONS"]["loaders"] = [  # type: ignore[index] # noqa F405
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    )
]

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Your stuff...
# ------------------------------------------------------------------------------

"""Schemas of the users views response."""

user_schema = {
    "email": {"type": "string", "required": True},
    "username": {"type": "string", "required": True},
    "first_name": {"type": "string", "required": False, "nullable": True},
    "last_name": {"type": "string", "required": False, "nullable": True},
    "is_staff": {"type": "boolean", "required": True},
}

user_login_schema = {
    "user": {"type": "dict", "required": True},
    "access_token": {"type": "string", "required": True},
}

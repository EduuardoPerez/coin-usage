"""Transactions response schemas."""
transactions_schema = {
    "created": {"type": "string", "required": True},
    "account_from": {"type": "string", "required": True},
    "account_to": {"type": "string", "required": True},
    "coin": {"type": "string", "required": True},
    "amount": {"type": "float", "required": True},
}

list_transactions_schema = {
    "type": "list",
    "empty": True,
    "required": True,
    "schema": {"type": "dict", "required": True, "schema": transactions_schema},
}

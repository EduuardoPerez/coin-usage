"""Accounts response schemas."""

balance_schema = {
    "coin": {"type": "string", "required": True},
    "amount": {"type": "float", "required": True},
}

account_balance_schema = {
    "address": {"type": "string", "required": True},
    "balances": {
        "type": "list",
        "required": True,
        "empty": True,
        "schema": {
            "type": "dict",
            "required": True,
            "schema": balance_schema,
        },
    },
}

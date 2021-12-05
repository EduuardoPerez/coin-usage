"""Schemas of the coins views response."""

coin_schema = {
    "ticker_symbol": {"type": "string", "required": True},
    "name": {"type": "string", "required": True},
}

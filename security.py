"""Helpers security (optionnels)."""


def sanitize_str(value: str) -> str:
    return (value or "").strip()


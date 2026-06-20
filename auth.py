"""Helpers auth (optionnels)."""


def require_login(session) -> bool:
    return bool(session.get("user"))


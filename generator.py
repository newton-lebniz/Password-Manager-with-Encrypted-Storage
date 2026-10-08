"""Secure random password generator."""

import secrets
import string


def generate_password(length=14, use_symbols=True):
    """Generate a secure random password."""

    if length < 8:
        raise ValueError("Password length must be at least 8.")

    characters = string.ascii_letters + string.digits

    if use_symbols:
        characters += "!@#$%^&*"

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password
#!/usr/bin/env python3
"""encrypting passwords module.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes password with a random salt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks whether hashed password was formed from the given password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

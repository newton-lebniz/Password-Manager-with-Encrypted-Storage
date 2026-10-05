"""Utilities for encrypting and decrypting password manager data"""

import base64
import os

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SALT_SIZE = 16
ITERATIONS = 480000

def generate_salt():
    """Generate and return a random salt"""
    return os.urandom(SALT_SIZE)

def derive_key(master_password,salt):
    """derive a fernet encryption key from the master password"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS,
    )

    key = kdf.derive(master_password.encode())
    return base64.urlsafe_b64encode(key)

def encrypt_data(text,key):
    """encrypt text using the supplied fernet key"""
    return Fernet(key).encrypt(text.encode())

def decrypt_data(token,key):
    """decrpty encrypted data and return the original text"""
    try:
        return Fernet(key).decrypt(token).decode()
    except InvalidToken:
        raise ValueError("Wrong master password or corrupted data")
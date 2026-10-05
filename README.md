# Password Manager with Encrypted Storage

A command-line password manager developed as an individual project for the CS213 Python course.

## Project Goal

The project will provide a local password vault where users can securely store and manage their credentials. Password data will be encrypted before being saved to disk.

## Day 1 - Encryption Foundation

Day 1 implements the cryptographic foundation of the password manager.

### Current Features

- Generate a random cryptographic salt.
- Derive an encryption key from a master password.
- Encrypt sensitive text using Fernet.
- Decrypt encrypted data.
- Detect an incorrect master password.
- Handle decryption errors using exception handling.

## Technologies

- Python
- `cryptography` library
- PBKDF2-HMAC
- SHA-256
- Fernet symmetric encryption

## Files

```text
crypto_utils.py
    Encryption and key-derivation functions.

test_crypto.py
    Tests encryption, decryption, and incorrect-password handling.

.gitignore
    Prevents sensitive and generated files from being committed.


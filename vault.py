"""Vault class for storing credentials in an encrypted file."""

import json
import os
from datetime import datetime

from crypto_utils import (
    SALT_SIZE,
    decrypt_data,
    derive_key,
    encrypt_data,
    generate_salt,
)


class Vault:
    """Manage password entries and store them in an encrypted file."""

    def __init__(self, path="vault.dat"):
        """Initialize a vault with a file path."""
        self.path = path
        self.entries = {}
        self._key = None
        self._salt = None

    def unlock(self, master_password):
        """Unlock an existing vault or create a new vault."""

        if os.path.exists(self.path):
            # Existing vault: read the encrypted file.
            try:
                with open(self.path, "rb") as file:
                    data = file.read()
            except OSError as error:
                raise IOError(f"Could not read vault: {error}")

            # First 16 bytes are the salt.
            if len(data) <= SALT_SIZE:
                raise ValueError("Vault file is corrupted.")

            self._salt = data[:SALT_SIZE]

            # Derive the same key using the supplied master password.
            self._key = derive_key(master_password, self._salt)

            # Decrypt everything after the salt.
            decrypted_text = decrypt_data(
                data[SALT_SIZE:],
                self._key
            )

            try:
                self.entries = json.loads(decrypted_text)
            except json.JSONDecodeError:
                raise ValueError("Vault data is corrupted.")

        else:
            # No vault exists, so create a new one.
            self._salt = generate_salt()
            self._key = derive_key(master_password, self._salt)
            self.entries = {}

            self.save()

    def save(self):
        """Encrypt the current entries and save them to the vault file."""

        if self._key is None or self._salt is None:
            raise ValueError("Vault is not unlocked.")

        text = json.dumps(self.entries)
        encrypted_data = encrypt_data(text, self._key)

        with open(self.path, "wb") as file:
            file.write(self._salt + encrypted_data)

    def add_entry(self, site, username, password, notes=""):
        """Add a new password entry to the vault."""

        site = site.strip().lower()

        if not site or not password:
            raise ValueError("Site and password cannot be empty.")

        if site in self.entries:
            raise ValueError(
                f"'{site}' already exists. Use update instead."
            )

        self.entries[site] = {
            "username": username,
            "password": password,
            "notes": notes,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }

        self.save()

    def get_entry(self, site):
        """Return the entry for a given site."""

        site = site.strip().lower()
        return self.entries[site]

    def delete_entry(self, site):
        """Delete an entry from the vault."""

        site = site.strip().lower()
        del self.entries[site]

        self.save()

    def list_sites(self):
        """Return all stored site names in alphabetical order."""

        return sorted(self.entries.keys())
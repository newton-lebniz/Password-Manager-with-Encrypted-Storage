"""Tests for the Vault class."""

import os

from vault import Vault


TEST_FILE = "test_vault.dat"


def cleanup():
    """Remove the temporary test vault."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def main():
    """Run basic Vault tests."""

    cleanup()

    vault = Vault(TEST_FILE)
    vault.unlock("master123")

    assert vault.list_sites() == []

    vault.add_entry(
        "github",
        "newton",
        "password123",
        "college project"
    )

    assert vault.list_sites() == ["github"]

    entry = vault.get_entry("github")

    assert entry["username"] == "newton"
    assert entry["password"] == "password123"

    try:
        vault.add_entry("github", "newton", "another")
        assert False, "Duplicate entry should raise ValueError"
    except ValueError:
        pass

    vault.delete_entry("github")

    assert vault.list_sites() == []

    cleanup()

    print("SUCCESS: Vault tests passed")


if __name__ == "__main__":
    main()
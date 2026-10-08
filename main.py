"""Command-line interface for the password manager."""

from getpass import getpass

from generator import generate_password
from vault import Vault


MENU = """
===== Password Manager =====
1. Add entry
2. View entry
3. Update entry
4. Delete entry
5. List all sites
6. Search
7. Generate password
8. Exit
"""


def mask(password):
    """Hide a password while displaying its length."""
    return "*" * len(password)


def add_entry(vault):
    """Add a new credential to the vault."""

    site = input("Site: ")
    username = input("Username: ")

    password = getpass("Password (leave empty to generate): ")

    if not password:
        password = generate_password()
        print("Generated password:", password)

    notes = input("Notes (optional): ")

    vault.add_entry(site, username, password, notes)
    print("Entry added successfully.")


def view_entry(vault):
    """Display one stored credential."""

    site = input("Site: ")
    entry = vault.get_entry(site)

    print("Username:", entry["username"])
    print("Password:", entry["password"])
    print("Notes:   ", entry["notes"])
    print("Created: ", entry["created"])


def update_entry(vault):
    """Update selected fields of an existing credential."""

    site = input("Site to update: ")

    # Check that the site exists before asking for new data.
    vault.get_entry(site)

    print("Leave a field empty to keep it unchanged.")

    username = input("New username: ")
    password = getpass("New password: ")
    notes = input("New notes: ")

    vault.update_entry(
        site,
        username,
        password,
        notes
    )

    print("Entry updated successfully.")


def delete_entry(vault):
    """Delete a credential after confirmation."""

    site = input("Site to delete: ")

    confirmation = input(
        f"Delete '{site}'? (y/n): "
    ).lower()

    if confirmation == "y":
        vault.delete_entry(site)
        print("Entry deleted successfully.")


def list_all(vault):
    """Display all stored sites without revealing passwords."""

    sites = vault.list_sites()

    if not sites:
        print("Vault is empty.")
        return

    for site in sites:
        entry = vault.entries[site]

        print(
            f"- {site} | "
            f"{entry['username']} | "
            f"{mask(entry['password'])}"
        )


def search_entries(vault):
    """Search for sites by site name or username."""

    keyword = input("Keyword: ")
    results = vault.search(keyword)

    if results:
        print("Found:", ", ".join(sorted(results)))
    else:
        print("No matching entries found.")


def main():
    """Start the password manager."""

    vault = Vault()

    master_password = getpass("Master password: ")

    try:
        vault.unlock(master_password)
    except (ValueError, IOError) as error:
        print("Error:", error)
        return

    actions = {
        "1": add_entry,
        "2": view_entry,
        "3": update_entry,
        "4": delete_entry,
        "5": list_all,
        "6": search_entries,
    }

    while True:
        print(MENU)

        choice = input("Choose an option: ").strip()

        if choice == "8":
            print("Goodbye!")
            break

        elif choice == "7":
            print("Generated password:", generate_password())

        elif choice in actions:
            try:
                actions[choice](vault)

            except KeyError:
                print("Error: site not found.")

            except ValueError as error:
                print("Error:", error)

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
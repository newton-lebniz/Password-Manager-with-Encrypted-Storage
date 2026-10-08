# 🔐 Password Manager with Encrypted Storage

A local command-line password manager built in Python as an individual project for the **CS213 Python course**.

The application provides a secure way to store and manage website credentials in an **encrypted local vault**. A master password is used to derive the encryption key, while individual passwords can be securely generated using Python's `secrets` module.

> **Educational project:** This application demonstrates Python programming, file handling, object-oriented programming, exception handling, modular design, and practical cryptography concepts.

---

## ✨ Features

### 🔑 Secure Vault
- Create a new encrypted password vault.
- Unlock an existing vault using a master password.
- Store credentials locally in encrypted form.
- Persist data between program executions.
- Detect incorrect master passwords or corrupted vault data.

### 🗂️ Credential Management
- Add new credentials.
- View stored credentials.
- Update existing credentials.
- Delete credentials with confirmation.
- Store usernames, passwords, notes, and creation timestamps.
- List all stored websites with passwords masked.
- Search credentials by website or username.

### 🎲 Password Generation
- Generate secure random passwords using Python's `secrets` module.
- Configure password length.
- Optionally include special characters.
- Prevent generation of passwords shorter than the minimum allowed length.

### 🛡️ Error Handling
- Handle incorrect master passwords.
- Detect corrupted vault files.
- Handle missing entries.
- Validate password input.
- Handle file-related errors using exceptions.

---

## 🔒 Security Design

The password manager uses several layers of protection.

### Master Password → Encryption Key

The master password is **not stored directly**.

Instead, the application derives an encryption key using:

```text
Master Password
       │
       ▼
 Random Salt
       │
       ▼
PBKDF2-HMAC-SHA256
       │
       ▼
 Encryption Key
       │
       ▼
Fernet Encryption
```

### Cryptographic Components

| Component | Purpose |
|---|---|
| **PBKDF2-HMAC-SHA256** | Derives a cryptographic key from the master password |
| **Random 16-byte salt** | Prevents identical passwords from producing identical derived keys |
| **Fernet** | Provides authenticated symmetric encryption |
| **`secrets` module** | Generates cryptographically secure random passwords |

The encrypted vault is stored locally as `vault.dat`.

The vault file is excluded from Git using `.gitignore` and is **never intended to be uploaded to the repository**.

### Forgotten Master Password

The current implementation does not provide password recovery.

This is intentional: because the master password is used to derive the encryption key, the application does not store the master password or a separate recovery key.

If the master password is lost, the encrypted vault cannot currently be recovered.

---

## 🧠 Python Concepts Demonstrated

The project demonstrates multiple concepts covered in the CS213 Python course.

| Python Concept | Implementation |
|---|---|
| **Control Flow** | CLI menu, loops, conditionals |
| **Functions** | Encryption, key derivation, CRUD operations, password generation |
| **Data Structures** | Dictionaries, nested dictionaries, sets |
| **File Handling** | Reading and writing the encrypted vault |
| **Exception Handling** | `try/except`, `ValueError`, `KeyError`, file errors |
| **Object-Oriented Programming** | `Vault` class |
| **Modules** | `crypto_utils`, `vault`, `generator`, `main` |
| **Third-Party Libraries** | `cryptography` |
| **Standard Library** | `os`, `json`, `datetime`, `secrets`, `string`, `getpass` |
| **Documentation** | Docstrings and comments |

---

## 🏗️ Project Structure

```text
Password-Manager-with-Encrypted-Storage/
│
├── main.py
│   └── Command-line interface and application menu
│
├── vault.py
│   └── Vault class and credential management
│
├── crypto_utils.py
│   └── Salt generation, key derivation,
│       encryption and decryption
│
├── generator.py
│   └── Secure random password generation
│
├── test_crypto.py
│   └── Encryption and decryption tests
│
├── test_vault.py
│   └── Vault storage and persistence tests
│
├── README.md
│   └── Project documentation
│
└── .gitignore
    └── Prevents sensitive and generated files
        from being committed
```

---

## ⚙️ Requirements

- **Python 3.10+**
- `cryptography`

Install the required third-party library:

```bash
pip install cryptography
```

---

## 🚀 Running the Application

Start the password manager with:

```bash
python3 main.py
```

On the first run, the application asks for a master password and creates an encrypted `vault.dat` file.

The application then provides the following menu:

```text
===== Password Manager =====
1. Add entry
2. View entry
3. Update entry
4. Delete entry
5. List all sites
6. Search
7. Generate password
8. Exit
```

### Example Workflow

```text
Master password: ********

===== Password Manager =====
1. Add entry
2. View entry
3. Update entry
4. Delete entry
5. List all sites
6. Search
7. Generate password
8. Exit

Choose an option: 1

Site: github
Username: newton
Password (leave empty to generate): ********
Notes (optional): Development account

Entry added successfully.
```

Passwords are masked when entries are listed:

```text
- github | newton | **************
```

---

## 🧪 Testing

### Encryption Tests

Run:

```bash
python3 test_crypto.py
```

The test verifies:

- Encryption produces encrypted data.
- Encrypted data can be decrypted correctly.
- Incorrect passwords are rejected.

### Vault Tests

Run:

```bash
python3 test_vault.py
```

The test verifies:

- Vault creation.
- Credential storage.
- Credential retrieval.
- Persistence.
- Incorrect-password handling.

### Syntax Check

All Python files can be checked with:

```bash
python3 -m py_compile \
crypto_utils.py \
vault.py \
generator.py \
main.py \
test_crypto.py \
test_vault.py
```

---

## 📈 Development Progress

The project was developed incrementally over multiple development stages.

### Day 1 — Cryptographic Foundation

Implemented the basic encryption layer:

- Random salt generation.
- PBKDF2-HMAC-SHA256 key derivation.
- Fernet encryption and decryption.
- Incorrect-password detection.
- Initial encryption tests.

### Day 2 — Encrypted Vault

Implemented the `Vault` class:

- Vault creation and unlocking.
- Encrypted file storage.
- Adding credentials.
- Retrieving credentials.
- Deleting credentials.
- Persistent storage.
- Vault tests.

### Day 3 — Complete CLI Application

Implemented the user-facing password manager:

- Credential updating.
- Credential searching.
- Secure password generation.
- Interactive command-line menu.
- Password masking.
- User input handling.
- Error handling.
- Complete end-to-end workflow.

---

## ⚠️ Limitations

This project is designed for educational purposes and has not undergone a professional security audit.

Current limitations include:

- No password recovery mechanism.
- No clipboard integration.
- No automatic password expiration.
- No multi-user support.
- No synchronization between devices.
- No professional security audit.
- Credentials are displayed in plaintext when the user explicitly chooses to view an entry.

These limitations provide opportunities for future development.

---

## 🔮 Possible Future Improvements

Potential extensions include:

- Password strength analysis.
- Clipboard integration with automatic clearing.
- Automatic vault locking after inactivity.
- More advanced password-generation rules.
- Import/export functionality.
- Backup and restore support.
- Encrypted cloud synchronization.
- Additional automated tests.
- A graphical user interface.

---

## 👨‍💻 Author

**Individual Project — CS213 Python Course**

Built using Python with a focus on practical application of Python programming concepts and secure local data storage.

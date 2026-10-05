"""test the encryption utilities"""

from crypto_utils import(
    generate_salt,
    derive_key,
    encrypt_data,
    decrypt_data,
)

def main():
    """Test encryption and decryption"""
    password = "my_master_password"
    secret = "my secret password"

    salt = generate_salt()
    key = derive_key(password,salt)

    encrypted = encrypt_data(secret,key)
    decrypted = decrypt_data(encrypted,key)

    print("original :",secret)
    print("encrypted:",encrypted)
    print("decrypted:",decrypted)

    if decrypted ==  secret:
        print("Success: encryption test passed")
    else:
        print("Error: encryption test failed")

    wrong_key = derive_key("wrong_password", salt)

    try:
        decrypt_data(encrypted, wrong_key)
        print("ERROR: Wrong password was accepted.")
    except ValueError as error:
        print("SUCCESS:", error)

if __name__ == "__main__":
    main()


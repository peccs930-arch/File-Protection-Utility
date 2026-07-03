import os
import base64
import hashlib
from cryptography.fernet import Fernet

def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_file(filename, password):
    key = generate_key(password)
    cipher = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = cipher.encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

    print("\nFile encrypted successfully.")
    print("Saved as:", filename + ".enc")

def decrypt_file(filename, password):
    key = generate_key(password)
    cipher = Fernet(key)

    try:
        with open(filename, "rb") as file:
            encrypted = file.read()

        decrypted = cipher.decrypt(encrypted)

        output = filename.replace(".enc", "_decrypted.txt")

        with open(output, "wb") as file:
            file.write(decrypted)

        print("\nFile decrypted successfully.")
        print("Saved as:", output)

    except:
        print("\nWrong password or invalid encrypted file.")

print("=" * 50)
print("        FILE PROTECTION UTILITY")
print("=" * 50)

print("1. Encrypt File")
print("2. Decrypt File")

choice = input("\nChoose Option: ")

if choice == "1":
    filename = input("Enter file name: ")
    password = input("Enter password: ")

    if os.path.exists(filename):
        encrypt_file(filename, password)
    else:
        print("File not found.")

elif choice == "2":
    filename = input("Enter encrypted file: ")
    password = input("Enter password: ")

    if os.path.exists(filename):
        decrypt_file(filename, password)
    else:
        print("File not found.")

else:
    print("Invalid option.")

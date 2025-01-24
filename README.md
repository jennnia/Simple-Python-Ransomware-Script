# Simple-Python-Ransomware-Script

🌟 This ransomware simulation script encrypts files in a specified folder and decrypts them only if the correct password is provided.

How It Works:

Key Generation: Creates and saves an encryption key (encryption_key.key).

File Encryption: Encrypts all files in the target folder using Fernet encryption.

Password Verification: Requires the correct password (r4ns0mw4r3 4tt4ck) to decrypt.

File Decryption: Restores the original files if the password is correct.

Use Case: Simulates ransomware behavior for educational purposes.

This script will work on any system (Windows, macOS, Linux) as long as the target folder path is valid for that specific operating system. Just ensure that:

✅ The target folder exists and has the correct file permissions.

✅ Python 3 and the cryptography module are installed on the system.

❗️Note: This script is intended only for educational purposes and is just simulating the attack, it won't fork for malicious purposes.

# Simple-Python-Malware-Scripts

🌟 Ransomware Simulation Script

Features:

Key Generation: Creates and saves an encryption key (encryption_key.key).

Key Transfer: Sends the key to the attacker cotrolled server.

File Encryption: Encrypts all files in the target folder using Fernet encryption.

Key Deletion: Deletes the encryption key on the target system.

File Decryption: Restores the original files if the provided key is correct.

Obfuscated Version: Includes an obfuscated variant for testing and evading detection.

Use Case: Simulates ransomware behavior for educational purposes.


🌟 Keylogger with Log Transmission and Concurrent Heart Display

This Python-based keylogger captures keystrokes and periodically sends the logs to a remote server. It runs concurrently with a program that displays hearts in the terminal as a fun touch. The keylogger uses the pynput library to capture keyboard inputs and sends logs every 200 seconds to a specified server.

Features:

Captures and logs keystrokes

Sends logs to a remote server every 200 seconds

Displays ASCII art and concurrently prints hearts in the terminal


🌟 Python Reverse Shell (RAT)

A simple Reverse Shell implemented in Python, where the client (victim) connects back to the server (attacker) and executes commands remotely.

Features:

Server: Listens for incoming client connections on a specified port and sends commands.

Client: Connects back to the server, executes received commands, and returns the output to the server.

Simple Command Execution: The server can send arbitrary commands to be executed on the client machine, with results returned to the attacker.

Base64 & Garbage Data Version: Client side code has been obfuscated with unnecessary variables, misleading function names, and random garbage data to make it harder to detect while Server side code was encoded using base64 encoding.


❗️Note: These scripts are intended only for educational purposes to understand how malware works. Don't misuse them for malicious purposes.

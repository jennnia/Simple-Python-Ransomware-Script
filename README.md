# Simple-Python-Malware-Scripts

🌟 Ransomware Simulation Script

How It Works:

Key Generation: Creates and saves an encryption key (encryption_key.key).

File Encryption: Encrypts all files in the target folder using Fernet encryption.

Password Verification: Requires the correct password (r4ns0mw4r3 4tt4ck) to decrypt.

File Decryption: Restores the original files if the password is correct.

Use Case: Simulates ransomware behavior for educational purposes.

This script will work on any system (Windows, macOS, Linux) as long as the target folder path is valid for that specific operating system. Just ensure that:

✅ The target folder exists and has the correct file permissions.

✅ Python 3 and the cryptography module are installed on the system.


🌟 Keylogger inside a Calculator Script

This Python script contains two main components:

Keylogger: A background keylogger that captures key presses and outputs them to the terminal. It's run using the pynput library.

Simple Calculator: A basic calculator that evaluates arithmetic expressions input by the user. It can handle basic operations like addition, subtraction, multiplication, and division.

The keylogger runs in the background while the calculator is active, capturing all key presses as the user interacts with the calculator.


🌟 Python Reverse Shell (RAT)

A simple Reverse Shell implemented in Python, where the client (victim) connects back to the server (attacker) and executes commands remotely.

Features:

Server: Listens for incoming client connections on a specified port and sends commands.

Client: Connects back to the server, executes received commands, and returns the output to the server.

Simple Command Execution: The server can send arbitrary commands to be executed on the client machine, with results returned to the attacker.

Base64 Encoded & Obfuscated Version: Includes an obfuscated, base64-encoded variant for testing and evading detection.


❗️Note: These scripts are intended only for educational purposes and are just simulating the attacks. They won't fork for malicious purposes.

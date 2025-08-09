# SecureEncryptorPro

Python GUI application for secure file encryption and decryption with master password protection, using symmetric encryption (Fernet).

## Features
- Master password authentication at startup
- AES-based symmetric encryption (Fernet)
- Encrypt and decrypt files with "Save As" dialogs
- Automatically saves encryption key to `.key` file
- Simple, user-friendly GUI with dark mode (customtkinter)
- Error handling and user notifications

## Usage
1. Run the app and enter the master password.
2. Select a file to encrypt or decrypt.
3. For encryption, select location to save encrypted `.enc` file and key file.
4. For decryption, select the encrypted file, key file, and output location for decrypted file.

## Requirements
- Python 3.8 or higher
- Install dependencies:
  ```bash
  pip install customtkinter cryptography

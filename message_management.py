from cryptography.fernet import Fernet
from dotenv import set_key
from pathlib import Path
import os

def check_keys(env_path: str, name_to_check: str):
    """
    ensure no doubles of key names exist.
    """
    if env_path.is_file():
        with open(env_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                key_name, _ = line.strip().split("=")
                if key_name == name_to_check:
                    return True
    return False

def generate_key(name: str):
    """
    Generate a key, save it as 'name' in
    .env file.
    """
    env_file_path = Path('.env')
    env_file_path.touch(mode=0o600, exist_ok=False)
    if check_keys(env_file_path, name):
        raise ValueError(f"A key with the name '{name}' already exists.")
    key = Fernet.generate_key()
    set_key(env_file_path, name, key)

def find_key(env_file_path: str, name: str):
    """
    Attempts to get key from file
    by its name
    """
    if env_file_path.is_file():
        with open(env_file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                key_name, key_value = line.strip().split("=")
                if key_name == name:
                    return key_value.encode()  # Return the key as bytes
    return False

def yield_key_names(env_file_path: str):
    """
    view what keys are saved/under
    what names they are saved.
    """
    if env_file_path.is_file():
        with open(env_file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                key_name, _ = line.strip().split("=")
                yield key_name

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message
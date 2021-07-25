from cryptography.fernet import Fernet, InvalidToken
from pathlib import Path

class Encryption():
    """description of class"""

    @staticmethod
    def generate_key():
        key_file = Path("encryption.key")
        if not key_file.is_file():
            f = open("encryption.key", "a+")
            f.close()
            key = Fernet.generate_key()
            print(key)
            with open("encryption.key", "wb") as key_file:
                key_file.write(key)
   
    @staticmethod
    def encrypt(item, key):
        print(key)
        message_bytes = bytes(item).encode()
        f = Fernet(key)
        return f.encrypt(message_bytes)

    @staticmethod
    def decrypt (item, key):
        try:
            if item != None:
                f = Fernet(key)
                item = item[2:-2]
                decrypted = f.decrypt(item)
                return decrypted
        except InvalidToken:
            print('The key is corrupted')

    @staticmethod
    def get_key():
        return open("encryption.key", "rb").read()
    


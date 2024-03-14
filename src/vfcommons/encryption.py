import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.fernet import Fernet, InvalidToken
from base64 import urlsafe_b64encode
from os import urandom


def derive_key(password: str, salt: bytes, iterations: int = 390000):
    try:
        kdf = Scrypt(
            salt=salt,
            length=32,
            n=2**14,
            r=8,
            p=1,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())
        return urlsafe_b64encode(key)
    except Exception as e:

        raise

def encrypt(data: str, password: str) -> str:
    try:
        salt = urandom(16)
        key = derive_key(password, salt)
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        result = base64.b64encode(salt + encrypted_data).decode('utf-8')

        return result
    except Exception as e:
        raise

def correct_padding(token: str) -> str:
    try:
        padding_needed = len(token) % 4
        if padding_needed:
            token += '=' * (4 - padding_needed)
        return token
    except Exception as e:
        raise

def decrypt(token: str, password: str) -> str:
    try:
        decoded_bytes = base64.b64decode(correct_padding(token))
        salt = decoded_bytes[:16]
        encrypted_data = decoded_bytes[16:]
        key = derive_key(password, salt)
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return decrypted_data
    except InvalidToken:
        raise
    except Exception as e:
        raise

import base64
import os
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hashes a password using bcrypt.

    :param password: The plaintext password to hash.
    :return: The hashed password.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a password against its hash.

    :param plain_password: The plaintext password to verify.
    :param hashed_password: The hashed password to verify against.
    :return: True if the password matches the hash, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def generate_secret(length: int = 16) -> str:
    """
    Generate a random secret key for OTP & token generation.

    Args:
        length (int): Length of the secret key. Default is 16 characters.

    Returns:
        str: A base32 encoded secret key.
    """
    secret = base64.b32encode(base64.b64encode(os.urandom(length))).decode('utf-8')
    return secret.rstrip('=')

from passlib.context import CryptContext

from app.services.base_service import BaseService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashService(BaseService):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

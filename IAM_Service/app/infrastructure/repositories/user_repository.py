from sqlalchemy.orm import Session
from typing import Annotated, Type

from app.core.db.database import get_db
from app.domain.models.user import User


class UserRepository:
    def __init__(self, db: Annotated[Session, get_db]):
        self.db = db

    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user_id: int, user: User) -> User:
        user.id = user_id
        self.db.merge(user)
        self.db.commit()
        return user

    def delete_user(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()
        self.db.flush()

    def get_user(self, user_id: int) -> Type[User] | None:
        return self.db.get(User, user_id)

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_mobile_number(self, mobile_number: str) -> User:
        return self.db.query(User).filter(User.mobile_number == mobile_number).first()

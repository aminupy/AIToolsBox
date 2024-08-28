from typing import Annotated, Dict
from uuid import UUID
from loguru import logger
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.domain.models.user import User


class UserRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        logger.info(f"User {user.id} created")
        return user

    def update_user(self, user_id: str, updated_user: Dict) -> User:
        # Update user with the given id
        user_query = self.db.query(User).filter(User.id == user_id)
        db_user = user_query.first()
        user_query.filter(User.id == user_id).update(
            updated_user, synchronize_session=False
        )
        self.db.commit()
        self.db.refresh(db_user)
        logger.info(f"User {user_id} updated")
        return db_user

    def delete_user(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()
        self.db.flush()
        logger.info(f"User {user.id} deleted")

    def get_user(self, user_id: UUID) -> User:
        logger.info(f"Fetching user {user_id}")
        return self.db.get(User, user_id)

    def get_user_by_email(self, email: str) -> User:
        logger.info(f"Fetching user with email {email}")
        return self.db.query(User).filter(User.email == email).first()

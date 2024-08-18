from fastapi_restful.guid_type import GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import Column, String, TIMESTAMP, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.db.database import get_entitybase
from app.domain.models.user_status import UserStatus

EntityBase = get_entitybase()


class User(EntityBase):
    __tablename__ = "users"

    id = Column(
        UUID,
        primary_key=True,
        index=True,
        unique=True,
        nullable=False,
        server_default=GUID_SERVER_DEFAULT_POSTGRESQL
    )
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    status = Column(Enum(UserStatus), nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, default=None, onupdate=func.now())

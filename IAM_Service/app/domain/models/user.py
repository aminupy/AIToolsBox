from fastapi_restful.guid_type import GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import Column, String, TIMESTAMP, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.core.db.database import get_entitybase

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
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    mobile_number = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_verified = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), nullable=True, default=None, onupdate=func.now())

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class TokenDataSchema(BaseModel):
    id: str
    first_name: str
    last_name: str
    mobile_number: str = Field(..., pattern=r"^\+?[1-9]\d{1,14}$")
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_verified: bool

    class Config:
        from_attributes = True

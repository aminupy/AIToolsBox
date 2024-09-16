from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class TokenUser(BaseModel):
    id: str
    fullname: str
    email: str

    class Config:
        from_attributes = True

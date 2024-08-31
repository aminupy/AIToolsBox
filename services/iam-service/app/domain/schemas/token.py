from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    access_token_expires: int
    refresh_token: str
    refresh_token_expires: int
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: Optional[str] = None
    type: Literal["access", "refresh"] = "access"
    exp: Optional[datetime] = None
    iat: Optional[datetime] = None



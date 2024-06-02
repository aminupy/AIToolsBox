from typing import Optional

from pydantic import BaseModel


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    mobile_number: Optional[str] = None


from typing import Optional

from pydantic import BaseModel, Field, EmailStr
from uuid import UUID


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    mobile_number = Field(..., regex=r'^\+?[1-9]\d{1,14}$')


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: UUID
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    email: Optional[str] = None

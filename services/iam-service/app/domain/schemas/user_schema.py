from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr

from app.domain.schemas.token_schema import TokenSchema


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    mobile_number: str = Field(..., pattern=r"^\+?[1-9]\d{1,14}$")


class UserCreateSchema(UserBaseSchema):
    password: str


class UserLoginSchema(BaseModel):
    mobile_number: str
    password: str


class UserSchema(UserBaseSchema):
    id: UUID
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    is_verified: bool

    class Config:
        from_attributes = True


class VerifyOTPSchema(BaseModel):
    mobile_number: str
    OTP: str


class ResendOTPSchema(BaseModel):
    mobile_number: str


class ResendOTPResponseSchema(BaseModel):
    mobile_number: str
    OTP: str
    message: str


class VerifyOTPResponseSchema(BaseModel):
    verified: bool
    message: str


class UserCreateResponseSchema(BaseModel):
    user: UserSchema
    OTP: str
    message: str


class UserLoginResponseSchema(BaseModel):
    user: UserSchema
    access_token: TokenSchema

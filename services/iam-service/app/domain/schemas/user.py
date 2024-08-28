from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr, constr

from app.domain.models.user_status import UserStatus


class UserBase(BaseModel):
    email: EmailStr


class UserInitialSignUp(UserBase):
    pass


class UserInitialSignUpResponse(UserBase):
    email: EmailStr
    status: UserStatus
    created_at: datetime
    message: str


class UserFinalSignUp(UserBase):
    fullname: constr(min_length=1, max_length=50)
    password: constr(min_length=8, max_length=50)


class UserSignIn(UserBase):
    password: constr(min_length=8, max_length=50)


class UserProfileUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[constr(min_length=3, max_length=50)] = None
    password: Optional[constr(min_length=8, max_length=50)] = None


class UserResponse(UserBase):
    id: UUID
    full_name: str
    status: UserStatus
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class UserInDB(UserBase):
    id: UUID
    full_name: str
    hashed_password: str
    status: UserStatus
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

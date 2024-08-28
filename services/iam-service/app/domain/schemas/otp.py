from pydantic import BaseModel, constr

from app.domain.models.user_status import UserStatus


class OTPRequest(BaseModel):
    email: constr(min_length=3, max_length=50)


class OTPResponse(BaseModel):
    message: str
    email: str
    expire_time: int


class OTPVerifyRequest(BaseModel):
    email: constr(min_length=3, max_length=50)
    otp: constr(min_length=6, max_length=6)


class OTPVerifyResponse(BaseModel):
    email: str
    status: UserStatus
    message: str



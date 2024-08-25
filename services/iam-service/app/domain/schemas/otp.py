from pydantic import BaseModel, constr


class OTPRequest(BaseModel):
    email: constr(min_length=3, max_length=50)


class OTPVerify(BaseModel):
    email: constr(min_length=3, max_length=50)
    otp: constr(min_length=6, max_length=6)


class OTPResponse(BaseModel):
    message: str
    email: str
    expire_time: int


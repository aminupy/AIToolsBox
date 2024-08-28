from enum import Enum


class UserStatus(str, Enum):
    UnVerified = "unverified"
    Verified = "verified"
    ACTIVE = "active"
    INACTIVE = "inactive"

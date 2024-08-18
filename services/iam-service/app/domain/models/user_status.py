from enum import Enum


class UserStatus(str, Enum):
    UnVerified = "unverified"
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"

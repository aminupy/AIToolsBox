class UserAlreadyExistsException(Exception):
    """Exception raised when trying to create a user that already exists."""
    def __init__(self, email: str):
        self.email = email
        self.message = f"User with email '{email}' already exists."
        super().__init__(self.message)


class OTPServiceException(Exception):
    """Exception raised when OTP service fails."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class UserNotFoundException(Exception):
    """Exception raised when user is not found."""
    def __init__(self, email: str):
        self.email = email
        self.message = f"User with email '{email}' not found."
        super().__init__(self.message)


class UserStatusException(Exception):
    """Exception raised when user status is invalid."""
    def __init__(self, status: str):
        self.status = status
        self.message = f"User is in invalid status: '{status}'."
        super().__init__(self.message)


class InvalidPasswordException(Exception):
    """Exception raised when user password is invalid."""
    def __init__(self, email: str):
        self.email = email
        self.message = f"Invalid password for email '{email}'."
        super().__init__(self.message)
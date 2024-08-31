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
    def __init__(self, user_identifier: str):
        self.email = user_identifier
        self.message = f"User '{user_identifier}' not found."
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


class InvalidGrantTypeException(Exception):
    """Exception raised when grant type is invalid."""
    def __init__(self, grant_type: str):
        self.grant_type = grant_type
        self.message = f"Invalid grant type: '{grant_type}'."
        super().__init__(self.message)


class UserMissMatchException(Exception):
    """Exception raised when user does not match."""
    def __init__(self, email: str, user_id: str):
        self.email = email
        self.message = f"User {user_id} does not match with email {email}."
        super().__init__(self.message)
from functools import wraps
from fastapi import HTTPException, status
from typing import Any, Callable
from loguru import logger

from app.core.exceptions import (
    UserAlreadyExistsException,
    UserStatusException,
    UserNotFoundException,
    InvalidPasswordException,
    OTPServiceException,
)


def handle_exceptions(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except UserAlreadyExistsException as e:
            logger.error(f"User already exists: {str(e)}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists.")
        except OTPServiceException as e:
            logger.error(f"OTP service error: {str(e)}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except UserNotFoundException as e:
            logger.error(f"User not found: {str(e)}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
        except UserStatusException as e:
            logger.error(f"User status issue: {str(e)}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except InvalidPasswordException as e:
            logger.error(f"Invalid password: {str(e)}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
        except Exception as e:
            logger.error(f"Unhandled exception in {func.__name__}: {str(e)}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

    return wrapper

from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.exceptions import (
    UserAlreadyExistsException,
    OTPServiceException,
    UserNotFoundException,
    UserStatusException, InvalidPasswordException
)
from app.domain.schemas.otp import OTPResponse, OTPVerify
from app.domain.schemas.token import Token
from app.domain.schemas.user import UserInitialSignUp, UserFinalSignUp, UserSignIn
from app.services import AuthService
from loguru import logger


class AuthController:
    def __init__(self, auth_service: Annotated[AuthService, Depends()]):
        self.auth_service = auth_service

    async def initialize_signup(self, user: UserInitialSignUp) -> OTPResponse:
        try:
            return await self.auth_service.initialize_signup(user)
        except UserAlreadyExistsException as e:
            logger.error(f"User already exists: {str(e)}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists.")
        except OTPServiceException as e:
            logger.error(f"OTP service error: {str(e)}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to send OTP.")
        except Exception as e:
            logger.error(f"Unhandled exception in initialize_signup: {str(e)}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

    async def verify_signup(self, otp_verify: OTPVerify) -> dict:
        try:
            return await self.auth_service.verify_signup(otp_verify)
        except OTPServiceException as e:
            logger.error(f"OTP verification error: {str(e)}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid OTP.")
        except UserNotFoundException as e:
            logger.error(f"User not found: {str(e)}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
        except Exception as e:
            logger.error(f"Unhandled exception in verify_signup: {str(e)}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

    async def finalize_signup(self, user: UserFinalSignUp) -> Token:
        try:
            return await self.auth_service.finalize_signup(user)
        except UserStatusException as e:
            logger.error(f"User status issue: {str(e)}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User status not valid for signup.")
        except UserNotFoundException as e:
            logger.error(f"User not found: {str(e)}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
        except Exception as e:
            logger.error(f"Unhandled exception in finalize_signup: {str(e)}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

    async def signin(self, user: UserSignIn) -> Token:
        try:
            return await self.auth_service.signin(user)
        except InvalidPasswordException as e:
            logger.error(f"Invalid password: {str(e)}")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
        except UserNotFoundException as e:
            logger.error(f"User not found: {str(e)}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
        except UserStatusException as e:
            logger.error(f"User status issue: {str(e)}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User status not valid for login.")
        except Exception as e:
            logger.error(f"Unhandled exception in signin: {str(e)}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

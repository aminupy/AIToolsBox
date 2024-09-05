from typing import Annotated
from fastapi import Depends, HTTPException, status

from app.core.security import TokenManager
from app.services import UserService
from app.utils.fastapi_utils import OAuth2PasswordBearerWithCookie
from app.domain.schemas.user import UserResponse


oauth2_access_scheme = OAuth2PasswordBearerWithCookie(
    tokenUrl="/auth/login", token_name="access_token"
)


async def get_current_user(
    token_manager: Annotated[TokenManager, Depends()],
    user_service: Annotated[UserService, Depends()],
    token: str = Depends(oauth2_access_scheme),
) -> UserResponse:
    token_payload = await token_manager.decode_token(token=token, token_type="access")
    if not token_payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = await user_service.get_user_by_email(token_payload.sub)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return UserResponse(
        id=user.id,
        email=user.email,
        fullname=user.fullname,
        status=user.status,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )

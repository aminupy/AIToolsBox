from app.services import AuthService, UserService, otp_service_provider
from app.services.sub_services.signup_service import SignUpService
from app.core.security import hash_provider
from app.infrastructure.repositories.user_repository import UserRepository
from app.db.database import session_local

from app.domain.schemas.user import UserInitialSignUp
from app.domain.schemas.otp import OTPVerify



async def run():
    signup_service = SignUpService(
        hash_service=hash_provider(),
        user_service=UserService(UserRepository(session_local()), hash_provider()),
        otp_service=otp_service_provider()
    )
    auth_service = AuthService(signup_service)

    # await signup_service.initialize_signup(UserInitialSignUp(email='amin@gmail.com'))
    await auth_service.verify_signup(OTPVerify(email='amin@gmail.com', otp="750659"))


if __name__ == '__main__':
    import asyncio
    # from app.db.database import init_db
    # init_db()
    asyncio.run(run())
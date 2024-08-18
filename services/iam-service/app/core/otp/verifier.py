import hmac
import time
from app.core.otp.generator import TOTPGenerator


class TOTPVerifier:
    def __init__(self, window: int = 1):
        self.generator = TOTPGenerator()
        self.window = window

    async def verify(self, otp: str, user_identifier: str, timestamp: int = None) -> bool:
        if timestamp is None:
            timestamp = int(time.time())

        # Verify the OTP within the allowed time window
        for offset in range(-self.window, self.window + 1):
            counter = timestamp + offset * self.generator.interval
            generated_otp = await self.generator.generate(user_identifier, counter)
            if hmac.compare_digest(generated_otp, otp):
                return True
        return False


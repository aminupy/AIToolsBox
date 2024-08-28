from typing import Annotated, Tuple
from fastapi import Depends
import hmac
import hashlib
import base64
import struct
import time

from app.core.config import get_settings, Settings


class TOTPGenerator:
    def __init__(self, config: Annotated[Settings, Depends(get_settings)]):
        self.base_secret = config.OTP_SECRET_KEY
        self.interval = config.OTP_EXPIRE_SECONDS  # Validity period in seconds
        self.digits = config.OTP_DIGITS

    async def _generate_hmac(self, counter: int, user_identifier: str) -> bytes:
        # Combine the base secret with a user-specific identifier
        combined_secret = f"{self.base_secret}{user_identifier}"
        key = base64.b32decode(base64.b32encode(combined_secret.encode()))
        counter_bytes = struct.pack(">Q", counter)
        hmac_hash = hmac.new(key, counter_bytes, hashlib.sha1).digest()
        return hmac_hash

    async def _truncate(self, hmac_hash: bytes) -> int:
        offset = hmac_hash[-1] & 0x0F
        binary = struct.unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF
        otp = binary % (10 ** self.digits)
        return otp

    async def generate(self, user_identifier: str, timestamp: int = None) -> tuple[str, int]:
        if timestamp is None:
            timestamp = int(time.time())
        counter = timestamp // self.interval
        hmac_hash = await self._generate_hmac(counter, user_identifier)
        otp = await self._truncate(hmac_hash)
        return str(otp).zfill(self.digits), self.interval - (timestamp % self.interval)


from datetime import datetime, timedelta

import jwt
from pwdlib import PasswordHash
from zoneinfo import ZoneInfo

from backend.settings import settings

pwd_context = PasswordHash.recommended()


class Hasher:
    """Wrap the hashes functionalities."""

    @staticmethod
    def get_password_hash(pwd: str) -> str:
        return pwd_context.hash(pwd)

    @staticmethod
    def verify_password(plain_pwd: str, hashed_pwd: str) -> bool:
        return pwd_context.verify(plain_pwd, hashed_pwd)


class JWT:
    """Wrap the encoding/decoding JWT token."""

    @staticmethod
    def encode(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
            settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

        to_encode.update({'exp': expire})

        encoded_jwt = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )

        return encoded_jwt

    @staticmethod
    def decode(token: str) -> dict:
        return jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )

from datetime import datetime, timedelta
from http import HTTPStatus
from typing import Annotated

import jwt
import sqlalchemy as sa
from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from zoneinfo import ZoneInfo

from backend import schemas
from backend.database import models
from backend.database.get_session import get_session
from backend.settings import settings

pwd_context = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')


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
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
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


def get_current_user(
    session: Annotated[Session, Depends(get_session)],
    token: Annotated[str, Depends(oauth2_scheme)],
):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    try:
        payload = JWT.decode(token)
        id = payload.get('sub')

        if not id:
            raise credentials_exception

        token_data = schemas.token.TokenData(id=id)
    except jwt.DecodeError:
        raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise credentials_exception

    user = session.scalar(
        sa.select(models.User).where(models.User.id == token_data.id)
    )

    if not user:
        raise credentials_exception

    return user

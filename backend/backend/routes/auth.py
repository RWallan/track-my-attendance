from http import HTTPStatus

import sqlalchemy as sa
from fastapi import APIRouter, HTTPException

from backend import deps, schemas, security
from backend.database import models

router = APIRouter(prefix='/auth')


@router.post('/token', response_model=schemas.token.Token)
def access_token(form_data: deps.OAuth2Form, session: deps.SessionDep):
    """Get new access token."""
    user = session.scalar(
        sa.select(models.User).where(models.User.email == form_data.username)
    )

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Incorrect email.'
        )

    if not security.Hasher.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Incorrect password.'
        )

    access_token = security.JWT.encode({'sub': user.id})

    return schemas.token.Token(token_type='bearer', access_token=access_token)

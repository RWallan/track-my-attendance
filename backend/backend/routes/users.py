import logging
from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from backend import crud, schemas
from backend.helpers import deps

router = APIRouter(prefix='/users')
logger = logging.getLogger('uvicorn')


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=schemas.users.User
)
def create_user(session: deps.SessionDep, user: schemas.users.CreateUser):
    """Create a new user."""
    user_db = crud.user.get_by_email(session, email=user.email)

    if user_db:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Email already exists.'
        )

    created_user = crud.user.create(session, user=user)

    return created_user


@router.put('/me', response_model=schemas.users.User)
def update_user(
    session: deps.SessionDep,
    user: schemas.users.UpdateUser,
    current_user: deps.CurrentUser,
):
    """Update user informations."""
    updated_user = crud.user.update(session, user=current_user, user_in=user)

    return updated_user


@router.delete('/me', response_model=schemas.msg.Message)
def delete_user(session: deps.SessionDep, current_user: deps.CurrentUser):
    """Delete user."""
    crud.user.delete(session, user=current_user)

    return schemas.msg.Message(message='User deleted')

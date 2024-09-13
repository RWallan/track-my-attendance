import logging
from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from backend import crud, deps, schemas

router = APIRouter(prefix='/users')
logger = logging.getLogger('uvicorn')


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=schemas.users.User
)
def create_user(session: deps.SessionDep, user: schemas.users.CreateUser):
    """Create a new user."""
    user_db = crud.user.get_by_email(session, email=user.email)

    if user_db:
        logger.error(f'Email {user.email} already exists.')
        print(f'Email {user.email} already exists.')
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail='Email already exists.'
        )

    created_user = crud.user.create(session, user=user)

    return created_user

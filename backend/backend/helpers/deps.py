from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.database import models
from backend.database.get_session import get_session
from backend.security import get_current_user

SessionDep = Annotated[Session, Depends(get_session)]
OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
CurrentUser = Annotated[models.User, Depends(get_current_user)]

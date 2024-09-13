import typing as T

import sqlalchemy as sa
from sqlalchemy.orm import Session

from backend.database import models
from backend.schemas import users
from backend.security import Hasher


class UserCRUD:
    """Execute the database operations in users table."""

    def __init__(self, model: T.Type[models.User]) -> None:
        self.model = model

    def get_user_by_email(
        self, session: Session, *, email: str
    ) -> T.Optional[models.User]:
        return session.scalar(
            sa.select(self.model).where(self.model.email == email)
        )

    def create_user(
        self, session: Session, *, user: users.CreateUser
    ) -> models.User:
        user.password = Hasher.get_password_hash(user.password)
        db_user = self.model(**user.model_dump())

        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return db_user


user = UserCRUD(models.User)

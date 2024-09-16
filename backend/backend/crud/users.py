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

    def get_by_email(
        self, session: Session, *, email: str
    ) -> T.Optional[models.User]:
        return session.scalar(
            sa.select(self.model).where(self.model.email == email)
        )

    def create(
        self, session: Session, *, user: users.CreateUser
    ) -> models.User:
        user.password = Hasher.get_password_hash(user.password)
        db_user = self.model(**user.model_dump())

        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return db_user

    @staticmethod
    def update(
        session, *, user: models.User, user_in: users.UpdateUser
    ) -> models.User:
        user_data = user_in.model_dump(exclude_unset=True)

        if 'password' in user_data:
            user_data['password'] = Hasher.get_password_hash(
                user_data['password']
            )

        for field in user_data:
            setattr(user, field, user_data[field])

        session.add(user)
        session.commit()
        session.refresh(user)

        return user

    @staticmethod
    def delete(session: Session, *, user: models.User):
        session.delete(user)
        session.commit()


user = UserCRUD(models.User)

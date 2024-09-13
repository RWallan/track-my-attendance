# type: ignore
import typing as T
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class BaseUser(BaseModel):
    name: T.Optional[str] = None
    email: T.Optional[EmailStr] = None
    course: T.Optional[str] = None
    period: T.Optional[str] = None


class CreateUser(BaseUser):
    name: str
    email: str
    course: str
    period: str
    password: str = Field(min_length=8, max_length=40)


class UserInDbBase(BaseUser):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    course: str
    period: str
    email: str
    created_at: datetime
    updated_at: datetime


class User(UserInDbBase):
    pass

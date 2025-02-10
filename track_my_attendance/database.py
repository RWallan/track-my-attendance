from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from track_my_attendance.settings import settings

engine = create_engine(settings.DATABASE_URL)


def get_session():  # pragma: nocover
    with Session(engine) as session:
        yield session

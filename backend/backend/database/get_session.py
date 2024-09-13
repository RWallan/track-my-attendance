from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from backend.settings import settings

engine = create_engine(settings.DATABASE_URL)


def get_session():  # pragma: nocover
    """Expose the Database Session."""
    with Session(engine) as session:
        yield session

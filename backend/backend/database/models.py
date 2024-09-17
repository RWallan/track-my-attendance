from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    course: Mapped[str]
    period: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=sa.func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=sa.func.now(), onupdate=sa.func.now()
    )


@table_registry.mapped_as_dataclass
class Course:
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    period: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=sa.func.now()
    )
    update_at: Mapped[datetime] = mapped_column(
        init=False, server_default=sa.func.now()
    )

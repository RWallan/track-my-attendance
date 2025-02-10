from datetime import date, datetime

from sqlalchemy import JSON, func
from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


# HACK: Must review start and end date to type correctly with DATE
@table_registry.mapped_as_dataclass
class Course:
    __tablename__ = 'courses'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str]
    start_date: Mapped[str]
    end_date: Mapped[str]
    schedule: Mapped[str]
    class_hours: Mapped[int]
    period: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, onupdate=func.now(), server_default=func.now()
    )

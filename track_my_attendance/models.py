from datetime import date, datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

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

    absences: Mapped[list['Absence']] = relationship(
        init=False, back_populates='course', cascade='all, delete-orphan'
    )


@table_registry.mapped_as_dataclass
class Absence:
    __tablename__ = 'absences'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    date: Mapped[datetime]
    present: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), onupdate=func.now()
    )

    course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'))
    course: Mapped[Course] = relationship(
        init=False, back_populates='absences'
    )

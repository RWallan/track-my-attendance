from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Day(Enum):
    monday = 'Monday'
    tuesday = 'Tuesday'
    wednesday = 'Wednesday'
    thursday = 'Thursday'
    friday = 'Friday'
    saturday = 'Saturday'
    sunday = 'Sunday'


class Schedule(BaseModel):
    day: Day
    start: str = Field(pattern=r'^\d{2}:\d{2}:\d{2}')
    end: str = Field(pattern=r'^\d{2}:\d{2}:\d{2}')

    model_config = ConfigDict(use_enum_values=True)


class BaseCourse(BaseModel):
    name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    schedule: Optional[list[Schedule]] = None
    class_hours: Optional[int] = None
    period: Optional[int] = None


class CourseSchema(BaseCourse):
    name: str  # type: ignore
    start_date: date  # type: ignore
    end_date: date  # type: ignore
    schedule: list[Schedule]  # type: ignore
    class_hours: int  # type: ignore
    period: int  # type: ignore


class CoursePublic(BaseCourse):
    start_date: str  # type: ignore
    end_date: str  # type: ignore
    schedule: str  # type: ignore
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CourseUpdate(BaseCourse):
    pass


class CourseList(BaseModel):
    courses: list[CoursePublic]


class Message(BaseModel):
    message: str

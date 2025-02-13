import json
from dataclasses import asdict
from datetime import datetime

from sqlalchemy import select

from track_my_attendance.models import Absence, Course


def test_create_course(session, mock_db_time):
    with mock_db_time(model=Course) as time:
        new_course = Course(
            name='course',
            start_date='2025-01-01',
            end_date='2025-01-02',
            schedule=json.dumps([
                {'day': 'Monday', 'start': '18:00:00', 'end': '19:00:00'}
            ]),
            class_hours=60,
            period=1,
        )

        session.add(new_course)
        session.commit()

        course = session.scalar(select(Course).where(Course.name == 'course'))

        assert asdict(course) == {
            'id': 1,
            'name': 'course',
            'start_date': '2025-01-01',
            'end_date': '2025-01-02',
            'schedule': '[{"day": "Monday", "start": "18:00:00", "end": "19:00:00"}]',  # noqa: E501
            'class_hours': 60,
            'created_at': time,
            'updated_at': time,
            'period': 1,
            'absences': [],
        }


def test_create_absence(session, course):
    new_absence = Absence(
        date=datetime.now(), present=True, course_id=course.id
    )

    session.add(new_absence)
    session.commit()
    session.refresh(new_absence)

    course = session.scalar(select(Course).where(Course.id == course.id))

    assert new_absence in course.absences

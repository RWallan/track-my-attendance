import json
from dataclasses import asdict

from sqlalchemy import select

from track_my_attendance.models import Course


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
        }

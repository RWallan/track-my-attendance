from http import HTTPStatus

from track_my_attendance.schemas import CoursePublic


def test_create_course(client):
    response = client.post(
        '/course',
        json={
            'name': 'course',
            'start_date': '2025-01-01',
            'end_date': '2025-02-02',
            'class_hours': 60,
            'schedule': [
                {'day': 'Monday', 'start': '18:00:00', 'end': '19:00:00'}
            ],
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['name'] == 'course'
    assert response.json()['class_hours'] == 60  # noqa: PLR2004 (Constant value)
    assert response.json()['start_date'] == '2025-01-01'
    assert response.json()['end_date'] == '2025-02-02'
    assert (
        response.json()['schedule']
        == "[{'day': 'Monday', 'start': '18:00:00', 'end': '19:00:00'}]"
    )


def test_get_courses(client, course):
    response = client.get('/course/')

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['courses']) == 1


def test_update_course(client, course):
    response = client.put(
        f'/course/{course.id}',
        json={
            'name': 'test',
            'class_hours': 90,
            'start_date': '2024-01-01',
            'end_date': '2024-01-02',
            'schedule': [
                {'day': 'Sunday', 'start': '12:00:00', 'end': '13:00:00'}
            ],
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['name'] == 'test'
    assert response.json()['class_hours'] == 90  # noqa: PLR2004 (Constant value)
    assert response.json()['start_date'] == '2024-01-01'
    assert response.json()['end_date'] == '2024-01-02'
    assert (
        response.json()['schedule']
        == "[{'day': 'Sunday', 'start': '12:00:00', 'end': '13:00:00'}]"
    )


def test_update_incorrect_course_must_raise(client):
    response = client.put(
        f'/course/20',
        json={
            'name': 'test',
            'class_hours': 90,
            'start_date': '2024-01-01',
            'end_date': '2024-01-02',
            'schedule': [
                {'day': 'Sunday', 'start': '12:00:00', 'end': '13:00:00'}
            ],
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Course not found'}


def test_delete_course(client, course):
    response = client.delete(f'/course/{course.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Course deleted'}


def test_delete_incorrect_course_must_raise(client):
    response = client.delete('/course/20')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Course not found'}

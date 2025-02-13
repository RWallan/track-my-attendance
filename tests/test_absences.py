from datetime import datetime
from http import HTTPStatus

import pytest

from tests.factories import AbsenceFactory


def test_create_absence(client, course):
    response = client.post(
        f'/absence/{course.id}',
        json={'date': datetime.now().isoformat(), 'present': True},
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json()['course_id'] == course.id
    assert response.json()['present']


def test_list_absences_should_return_5(session, client, course):
    expected_absences = 5
    session.bulk_save_objects(
        AbsenceFactory.create_batch(5, course_id=course.id)
    )
    session.commit()

    response = client.get('/absence/')

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['absences']) == expected_absences


def test_list_absences_should_return_2(session, client, course):
    expected_absences = 2
    session.bulk_save_objects(
        AbsenceFactory.create_batch(5, course_id=course.id)
    )
    session.commit()

    response = client.get(
        '/absence/',
        params={'limit': 2, 'offset': 1},
    )

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['absences']) == expected_absences


def test_list_absences_with_filters(session, client, course):
    expected_absences = 5

    session.bulk_save_objects(
        AbsenceFactory.create_batch(
            5, course_id=course.id, present=True, date=datetime.now()
        )
    )
    session.commit()

    response = client.get(
        '/absence/',
        params={
            'course_id': course.id,
            'present': True,
            'start_date': datetime(2024, 1, 1),
            'end_date': datetime(2099, 2, 2),
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['absences']) == expected_absences


def test_list_absences_with_wrong_course_must_raise(session, client):
    session.bulk_save_objects(AbsenceFactory.create_batch(5))
    session.commit()

    response = client.get('/absence/', params={'course_id': 999})

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_patch_absence(session, client, course):
    session.bulk_save_objects(
        AbsenceFactory.create_batch(5, course_id=course.id)
    )
    session.commit()

    response = client.patch(
        '/absence/1/1', json={'date': datetime(2023, 1, 1).isoformat()}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['date'] == datetime(2023, 1, 1).isoformat()


def test_delete_absence(session, client, course):
    session.bulk_save_objects(
        AbsenceFactory.create_batch(5, course_id=course.id)
    )
    session.commit()

    response = client.delete('/absence/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['message'] == 'Absence deleted'

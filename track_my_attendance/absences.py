from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from track_my_attendance.database import get_session
from track_my_attendance.models import Absence, Course
from track_my_attendance.schemas import (
    AbsenceList,
    AbsencePublic,
    AbsenceSchema,
    AbsenceUpdate,
    FilterAbsence,
    Message,
)

router = APIRouter()


@router.get('/absence/', response_model=AbsenceList)
def list_absences(
    absence_filter: Annotated[FilterAbsence, Query()],
    session: Session = Depends(get_session),
):
    query = select(Absence)
    if absence_filter.course_id:
        course = session.scalar(
            select(Course).where(Course.id == absence_filter.course_id)
        )

        if not course:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='Course not found'
            )

        query = query.filter(Absence.course_id == absence_filter.course_id)

    if absence_filter.start_date:
        query = query.filter(Absence.date >= absence_filter.start_date)

    if absence_filter.end_date:
        query = query.filter(Absence.date <= absence_filter.end_date)

    if absence_filter.present:
        query = query.filter(Absence.present == absence_filter.present)

    absences = session.scalars(
        query.offset(absence_filter.offset).limit(absence_filter.limit)
    ).all()

    return {'absences': absences}


@router.post(
    '/absence/{course_id}',
    status_code=HTTPStatus.CREATED,
    response_model=AbsencePublic,
)
def create_absence(
    course_id: int,
    absence: AbsenceSchema,
    session: Session = Depends(get_session),
):
    print('aaaa')
    course = session.scalar(select(Course).where(Course.id == course_id))

    if not course:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Course not found'
        )

    new_absence = Absence(
        date=absence.date, present=absence.present, course_id=course_id
    )
    session.add(new_absence)
    session.commit()
    session.refresh(new_absence)

    return new_absence


@router.patch('/absence/{course_id}/{id}', response_model=AbsencePublic)
def patch_absence(
    course_id: int,
    id: int,
    absence: AbsenceUpdate,
    session: Session = Depends(get_session),
):
    course = session.scalar(select(Course).where(Course.id == course_id))

    if not course:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Course not found'
        )

    if absence.course_id:
        course = session.scalar(
            select(Course).where(Course.id == absence.course_id)
        )

        if not course:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='New course not found'
            )

    db_absence = session.scalar(select(Absence).where(Absence.id == id))
    if not db_absence:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Absence not found'
        )

    for key, value in absence.model_dump(exclude_unset=True).items():
        setattr(db_absence, key, value)

    session.commit()
    session.refresh(db_absence)

    return db_absence


@router.delete('/absence/{id}', response_model=Message)
def delete_absence(id: int, session: Session = Depends(get_session)):
    db_absence = session.scalar(select(Absence).where(Absence.id == id))
    if not db_absence:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Absence not found'
        )
    session.delete(db_absence)
    session.commit()
    return {'message': 'Absence deleted'}

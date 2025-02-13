from datetime import datetime
from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from track_my_attendance.database import get_session
from track_my_attendance.models import Course
from track_my_attendance.schemas import (
    CourseList,
    CoursePublic,
    CourseSchema,
    CourseUpdate,
)

router = APIRouter()


@router.post(
    '/course/', status_code=HTTPStatus.CREATED, response_model=CoursePublic
)
def create_course(
    course: CourseSchema, session: Session = Depends(get_session)
):
    # HACK: Transform to str because sqlite don't accept date and json columns
    # or it's just because I don't know how to create it
    db_course = Course(
        name=course.name,
        start_date=course.start_date.strftime('%Y-%m-%d'),
        end_date=course.end_date.strftime('%Y-%m-%d'),
        class_hours=course.class_hours,
        schedule=str(course.model_dump()['schedule']),
        period=course.period,
    )
    session.add(db_course)
    session.commit()
    session.refresh(db_course)

    return db_course


@router.get('/course/', response_model=CourseList)
def get_courses(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    courses = session.scalars(select(Course).offset(skip).limit(limit)).all()

    return {'courses': courses}


@router.put(
    '/course/{id}', status_code=HTTPStatus.CREATED, response_model=CoursePublic
)
def update_course(
    id: int, course: CourseUpdate, session: Session = Depends(get_session)
):
    course_db = session.scalar(select(Course).where(Course.id == id))
    if not course_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Course not found'
        )
    data = course.model_dump(exclude_unset=True)

    # HACK: Transform to str because sqlite don't accept date and json columns
    # or it's just because I don't know how to create it
    if 'schedule' in data:
        data['schedule'] = str(data['schedule'])

    if 'start_date' in data:
        data['start_date'] = data['start_date'].strftime('%Y-%m-%d')

    if 'end_date' in data:
        data['end_date'] = data['end_date'].strftime('%Y-%m-%d')

    for key, value in data.items():
        setattr(course_db, key, value)

    session.commit()
    session.refresh(course_db)

    return course_db


@router.delete('/course/{id}')
def delete_course(id: int, session: Session = Depends(get_session)):
    course_db = session.scalar(select(Course).where(Course.id == id))

    if not course_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Course not found'
        )

    session.delete(course_db)
    session.commit()

    return {'message': 'Course deleted'}

from sqlalchemy.orm import Session
from app.schemas.course import CourseCreate
from app.repository import course_repository


def create_course(course_data: CourseCreate, db: Session):

    return course_repository.create_course(
        course_data,
        db
    )


def get_all_courses(db: Session):

    return course_repository.get_all_courses(db)


def get_course_by_id(course_id: int, db: Session):

    return course_repository.get_course_by_id(
        course_id,
        db
    )
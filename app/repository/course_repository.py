from sqlalchemy.orm import Session
from app.models.course import Course
from app.schemas.course import CourseCreate


def create_course(course_data: CourseCreate, db: Session):

    new_course = Course(
        course_name=course_data.course_name
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course


def get_all_courses(db: Session):

    courses = db.query(Course).all()

    return courses


def get_course_by_id(course_id: int, db: Session):

    course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    return course
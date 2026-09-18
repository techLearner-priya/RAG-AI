from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.course import Course
from app.models.student import Student

from app.schemas.student import StudentCreate
from app.repository import student_repository


def create_student(student_data: StudentCreate, db: Session):
    db_student = Student(
        student_name=student_data.name,
        student_age=student_data.age,
        grade=student_data.grade,
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student



def get_all_students(db: Session):

    return student_repository.get_all_students(db)


def get_student_by_id(student_id: int, db: Session):

    return student_repository.get_student_by_id(
        student_id,
        db
    )


def add_course_to_student(
    student_id: int,
    course_id: int,
    db: Session
):

    db_student = get_student_by_id(student_id, db)
    db_course = db.query(Course).filter(Course.id == course_id).first()

    if db_student is None:
        raise HTTPException(status_code=404, detail=f"Student {student_id} not found")

    if db_course is None:
        raise HTTPException(status_code=404, detail=f"Course {course_id} not found")

    if db_course not in db_student.courses:
        db_student.courses.append(db_course)
        db.commit()
        db.refresh(db_student)

    return db_student
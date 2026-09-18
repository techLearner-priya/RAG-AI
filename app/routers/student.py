from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.student import StudentCreate
from app.service import student as student_service

router = APIRouter()


@router.post("/students")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return student_service.create_student(student, db)


@router.get("/students")
def get_all_students(
    db: Session = Depends(get_db)
):
    return student_service.get_all_students(db)


@router.get("/students/{student_id}")
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):
    return student_service.get_student_by_id(student_id, db)


@router.post("/students/{student_id}/courses/{course_id}")
def add_course_to_student(
    student_id: int,
    course_id: int,
    db: Session = Depends(get_db)
):
    return student_service.add_course_to_student(
        student_id,
        course_id,
        db
    )
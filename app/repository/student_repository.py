from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.course import Course
from app.models.student import Student



def get_all_students(db: Session):
    return db.query(Student).all()


def get_student_by_id(student_id: int, db: Session):
    return db.query(Student).filter(Student.id == student_id).first()


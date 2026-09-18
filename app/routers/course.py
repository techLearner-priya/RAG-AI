from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.course import CourseCreate
from app.service import course as course_service


router = APIRouter()


@router.post("/courses")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    return course_service.create_course(course, db)


@router.get("/courses")
def get_all_courses(db: Session = Depends(get_db)):
    return course_service.get_all_courses(db)


@router.get("/courses/{course_id}")
def get_course_by_id(course_id: int, db: Session = Depends(get_db)):
    return course_service.get_course_by_id(course_id, db)
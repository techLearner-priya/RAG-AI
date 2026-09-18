from fastapi import FastAPI

from app.database.database import engine, Base

from app.models.student import Student
from app.models.course import Course
from app.models.student_course import student_course
from app.routers import student, course

app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(student.router)
app.include_router(course.router)


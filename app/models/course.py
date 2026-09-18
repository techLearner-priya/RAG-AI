from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.database.database import Base
from app.models.student_course import student_course

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    course_name = Column(String)

    students = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses"
    )

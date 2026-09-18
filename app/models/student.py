from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import relationship


from app.database.database import Base
from app.models.student_course import student_course

class Student(Base):

    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    student_name = Column(String)
    student_age = Column(Integer)
    grade = Column(String)

    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates="students"
    )
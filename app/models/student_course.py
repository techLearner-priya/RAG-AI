from sqlalchemy import Column, ForeignKey, Integer, Table

from app.database.database import Base


student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("student.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("course.id"), primary_key=True),
)
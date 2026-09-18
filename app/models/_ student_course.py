from sqlalchemy import Table, Column, Integer, ForeignKey

from app.database.database import Base


student_course = Table(
    "student_course",
    Base.metadata,

    Column(
        "student_id",
        Integer,
        ForeignKey("student.id")
    ),

    Column(
        "course_id",
        Integer,
        ForeignKey("course.id")
    )
)
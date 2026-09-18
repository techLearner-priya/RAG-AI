from sqlalchemy import Column, Integer, String
from app.database.database import Base


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    file_path = Column(String)
    content_type = Column(String)


import os
import shutil
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database.database import get_db
from app.schemas.user import UserCreate, UserUpdate
from app.repository import user_repository
from app.models.file import File as FileModel


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# CREATE USER
def createUser(user :user_create , db : Session ):
    user = user_repository.createUser(user,db)
    return user

# UPDATE USER
def UpdateUser(user_id: int, user : UserUpdate, db : Session ):
    user = user_repository.updateUser(user_id, user, db)
    return user

#delete user
def deleteByUserId(user_id : int, db : Session ):
    return user_repository.deleteByUserId(user_id,db)


def upload_file(
    file: UploadFile , db: Session ):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    new_file = FileModel(
        filename=file.filename,
        file_path=file_path,
        content_type=file.content_type
    )

    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return new_file



def get_file(
    file_id: int,
    db: Session 
):

    file = db.query(FileModel).filter(
        FileModel.id == file_id
    ).first()

    if file is None:
        return {"message": "File not found"}

    return os.path.abspath(file.file_path)
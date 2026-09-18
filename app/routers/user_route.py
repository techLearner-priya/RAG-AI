from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os
from app.database.database import get_db
from app.schemas.user import UserCreate,UserUpdate
from app.service import user_service

router = APIRouter()

@router.get("/")
def home():
    return {"message" : "hello, i learn python"}

@router.post("/users")
def create_User(user : UserCreate, db : Session = Depends(get_db)):

    new_user = user_service.createUser(user,db)
    return new_user

@router.put("/user/{user_id}")
def UpdateUser(user_id: int, user : UserUpdate, db : Session = Depends(get_db)):

    UpdateUser = user_service.UpdateUser(user_id,user,db)
    return    UpdateUser

@router.delete("/user/{user_id}")
def deleteByUserId(user_id : int, db : Session = Depends(get_db)):

    return user_service.deleteByUserId(user_id,db)


    
@router.post("/document")
def UploadDocument(file: (UploadFile) = File(...), db: Session = Depends(get_db)):
   
  

     if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF allowed")

     return user_service.upload_file(file, db)


@router.get("/document/{file_id}")
def getDocument(file_id: int, db: Session = Depends(get_db)):
    file = user_service.get_file(file_id, db)
    if file is None:
        return {"message": "File not found"}

    return FileResponse(path=file, filename=os.path.basename(file))



    
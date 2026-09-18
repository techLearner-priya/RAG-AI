from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.database.database import get_db
from app.schemas.user import UserCreate, UserUpdate


def getUserById(user_id : int , db: Session ):
    return db.query(User).filter(User.id == user_id).first()


def createUser(user: UserCreate, db: Session ):
    db_user = User(
        name=user.name,
        email=user.email,
        country=user.country,
        age=user.age
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def updateUser(user_id: int, user: UserUpdate, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return None

    db_user.name = user.name
    db_user.email = user.email
    db_user.country = user.country
    db_user.age = user.age

    db.commit()
    db.refresh(db_user)
    return db_user


def deleteByUserId(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return None
    
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}



def findUserBetweenAges(startAge: int, endAge: int, db: Session):
    return db.query(User).filter(User.age >= startAge, User.age <= endAge).all()


def findUserInCountry(country: str, db: Session):
    return db.query(User).filter(User.country == country).all()



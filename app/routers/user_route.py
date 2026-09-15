from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Hello, I am learning FastAPI"}


@router.get("/about")
def about():
    return {"message": "Priya is my name"}


@router.get("/myself")
def myself():
    return {"message": "Priya is my name"}


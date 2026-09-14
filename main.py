from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, I am learning FastAPI"}


@app.get("/about")
def about():
    return {"priya is my name"}



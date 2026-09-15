from fastapi import FastAPI
from app.routers import user_route

app = FastAPI()

app.include_router(user_route.router)

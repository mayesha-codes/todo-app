from fastapi import FastAPI
from .routers import users, todos,sub_todos
from . import models
from .database import  engine
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

#Include routers
app.include_router(users.router)
app.include_router(todos.router)
app.include_router(sub_todos.router)

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Todo App"}
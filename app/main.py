from fastapi import FastAPI
from .routers import users, todos,sub_todos
from .models import Base
from .database import  engine
Base.metadata.create_all(bind=engine)


app = FastAPI()

#Include routers
app.include_router(users.router)
app.include_router(todos.router)
app.include_router(sub_todos.router)

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI Todo App"}
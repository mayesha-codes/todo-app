from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db  # Ensure get_db is inside database.py


router = APIRouter()


# ✅ Route to Get Todos
@router.get("/todos/", response_model=list[schemas.Todo])
def get_todos(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
    todos = crud.get_todos(db,skip=skip,limit=limit)
    return todos
from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db  # Ensure get_db is inside database.py


router = APIRouter()

# ✅ Route to Create a todo by a specific user
@router.post("/users/{user_id}/todos/",response_model=schemas.Todo)
def post_todo_for_user(user_id:int, todo:schemas.TodoCreate, db:Session=Depends(get_db)):
    return crud.create_todo(db=db,todo=todo,owner_id=user_id)

# ✅ Route to Get Todo by id
@router.get("/todo/{todo_id}/", response_model=schemas.Todo)
def get_todo(todo_id:int,db:Session=Depends(get_db)):
    todo = crud.get_todo(db,todo_id=todo_id)
    return todo

# ✅ Route to Get Todos for a user
@router.get("/todos/{owner_id}/", response_model=list[schemas.Todo])
def get_todos_by_user(owner_id:int,skip:int=0,limit:int=10,db:Session=Depends(get_db)):
    user_todos = crud.get_todos_by_user(db,owner_id=owner_id,skip=skip,limit=limit)
    return user_todos

# ✅ Route to update a Todo by id
@router.patch("/todo/{todo_id}/", response_model=schemas.Todo)
def update_todo(todo_id:int,todo_update:schemas.TodoUpdate,db:Session=Depends(get_db)):
    updated_todo = crud.update_todo(db,todo_id=todo_id,todo_update=todo_update)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

# ✅ Route to delete a Todo by id
@router.delete("/todo/{todo_id}",response_model=schemas.Todo)
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    deleted_todo=crud.delete_todo(db,todo_id=todo_id)
    if not deleted_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return deleted_todo

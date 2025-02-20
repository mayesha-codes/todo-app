from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas,ai
from app.database import get_db  # Ensure get_db is inside database.py


router = APIRouter()


# ✅ Route to generate a SubTodo for a specific todo by ai model
@router.post("todo/{todo_id}/generate_subtodo/")
def generate_subtodo(todo_id:int,sub_todo:schemas.SubTodoCreate,db:Session=Depends(get_db)):
    #check if the parent todo exist
    parent_todo=crud.get_todo(db,todo_id=todo_id)
    if not parent_todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    # Generate subtodos using AI
    gen_subtodo=ai.generate_subtodos(parent_todo.title,parent_todo.description)
    # Save generated sub-todos
    created_subtodos=[]
    for gen_subtodo in gen_subtodo:
        sub_todo=crud.create_subtodo(db,parent_todo_id=todo_id,sub_todo=sub_todo)
        created_subtodos.append(sub_todo)
    return created_subtodos
# ✅ Route to create a SubTodo for a specific todo
@router.post("todo/{todo_id}/subtodo/",response_model=schemas.SubTodo)
def create_subtodo(todo_id:int,sub_todo:schemas.SubTodoCreate,db:Session=Depends(get_db)):
    #check if the parent todo exist
    parent_todo=crud.get_todo(db,todo_id=todo_id)
    if not parent_todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    
    return crud.create_subtodo(db,parent_todo_id=todo_id,sub_todo=sub_todo)

# ✅ Route to Get SubTodos for a Todo
@router.get("/todos/subtodos/{parent_todo_id}/", response_model=list[schemas.SubTodo])
def get_subtodos_for_todo(parent_todo_id:int,db:Session=Depends(get_db)):
    todo_subtodos = crud.get_subtodos_for_todo(db,owner_id=parent_todo_id)
    return todo_subtodos

# ✅ Route to update a SubTodo by id
@router.patch("/todo/subtodo/{subtodo_id}/", response_model=schemas.SubTodo)
def update_subtodo(subtodo_id:int,subtodo_update:schemas.SubTodoUpdate,db:Session=Depends(get_db)):
    updated_subtodo = crud.update_subtodo(db,subtodo_id=subtodo_id,subtodo_update=subtodo_update)
    if not updated_subtodo:
        raise HTTPException(status_code=404, detail="subTodo not found")
    return updated_subtodo

# ✅ Route to delete a SubTodo by id
@router.delete("/todo/subtodo/{subtodo_id}",response_model=schemas.SubTodo)
def delete_subtodo(subtodo_id:int,db:Session=Depends(get_db)):
    deleted_subtodo=crud.delete_subtodo(db,subtodo_id=subtodo_id)
    if not deleted_subtodo:
        raise HTTPException(status_code=404, detail="SubTodo not found")
    return deleted_subtodo


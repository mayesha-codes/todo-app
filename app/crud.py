from sqlalchemy.orm import Session
from app.models import User, Todo
from app.schemas import *
from typing import List, Optional



# ✅ Create a new user
def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ✅ Get a user by ID
def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.user_id == user_id).first()

# ✅ Get all users
def get_users(db: Session,skip:int=0,limit:int=10) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()

###################################################################TODO_CRUD####################################################

# ✅ Create a new todo
def create_todo(db: Session, todo: TodoCreate, owner_id: int):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        thumbnail=todo.thumbnail,
        due_date_time=todo.due_date_time,
        owner_id=owner_id,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# ✅ Get a todo by ID
def get_todo(db: Session, todo_id: int) -> Optional[Todo]:
    return db.query(Todo).filter(Todo.todo_id == todo_id).first()

# ✅ Get all todos for a user
def get_todos_by_user(db: Session, owner_id: int,skip:int=0,limit:int=10) -> List[Todo]:
    return db.query(Todo).filter(Todo.owner_id == owner_id).offset(skip).limit(limit).all()

# ✅ Update a todo
def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate):
    db_todo = db.query(Todo).filter(Todo.todo_id == todo_id).first()
    if not db_todo:
        return None
    # Update only provided fields
    for key, value in todo_update.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# ✅ Delete a todo
def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(Todo).filter(Todo.todo_id == todo_id).first()
    if not db_todo:
        return None
    db.delete(db_todo)
    db.commit()
    return db_todo
    
###############################################SUB_TODO_CRUD################################################
# ✅ Create new subtodo
def create_subtodo(db: Session, subtodo: SubTodoCreate, parent_todo_id: int):
    db_subtodo = SubTodo(
        title=subtodo.title,
        description=subtodo.description,
        thumbnail=subtodo.thumbnail,
        duration=subtodo.duration,
        owner_id=parent_todo_id,
    )
    db.add(db_subtodo)
    db.commit()
    db.refresh(db_subtodo)
    return db_subtodo

# ✅ Get all subtodos for a todo
def get_subtodos_for_todo(db: Session, parent_todo_id: int) -> List[SubTodo]:
    return db.query(SubTodo).filter(SubTodo.owner_id == parent_todo_id).all()

# ✅ Update a sub todo
def update_subtodo(db: Session, subtodo_id: int, subtodo_update: SubTodoUpdate):
    db_subtodo = db.query(SubTodo).filter(SubTodo.subtodo_id == subtodo_id).first()
    if not db_subtodo:
        return None
    # Update only provided fields
    for key, value in subtodo_update.dict(exclude_unset=True).items():
        setattr(db_subtodo, key, value)
    db.commit()
    db.refresh(db_subtodo)
    return db_subtodo

# ✅ Delete a subtodo
def delete_subtodo(db: Session, subtodo_id: int):
    db_subtodo = db.query(SubTodo).filter(SubTodo.subtodo_id == subtodo_id).first()
    if not db_subtodo:
        return None
    db.delete(db_subtodo)
    db.commit()
    return db_subtodo
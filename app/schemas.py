from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# ✅ Base schema for SubTodo (Shared fields)
class SubTodoBase(BaseModel):
    title: str
    description: str
    thumbnail: Optional[str] = None
    duration: int 


# ✅ Schema for Creating a SubTodo (Request)
class SubTodoCreate(SubTodoBase):
    pass  # No extra fields required for creation

# ✅ Schema for Updating a SubTodo (Request)
class SubTodoUpdate(SubTodoBase):
    title: Optional[str] = None
    description: Optional[str] = None
    thumbnail: Optional[str] = None
    duration:Optional[int]=None

# ✅ Schema for SubTodo Response (Includes `id`, timestamps, and `owner_id`)
class SubTodo(SubTodoBase):
    subtodo_id: int
    created_at: datetime
    updated_at: datetime
    parent_todo_id: int  # Foreign key linking to Todo
    duration:int
    class Config:
        orm_mode = True  # Allows SQLAlchemy model conversion



# ✅ Base schema for Todo (Shared fields)
class TodoBase(BaseModel):
    title: str
    description: str
    thumbnail: Optional[str] = None
    due_date_time: datetime  # Due date and time is required
    duration: int

# ✅ Schema for Creating a Todo (Request)
class TodoCreate(TodoBase):
    pass  # No extra fields required for creation

# ✅ Schema for Updating a Todo (Request)
class TodoUpdate(TodoBase):
    title: Optional[str] = None
    description: Optional[str] = None
    thumbnail: Optional[str] = None
    due_date_time: Optional[datetime] = None
    duration:Optional[int]=None

# ✅ Schema for Todo Response (Includes `id`, timestamps, and `owner_id`)
class Todo(TodoBase):
    todo_id: int
    created_at: datetime
    updated_at: datetime
    parent_user_id: int  # Foreign key linking to User
    duration:int
    subtodos: List[SubTodo] = []  # todo has multiple subtodos
    class Config:
        orm_mode = True  # Allows SQLAlchemy model conversion

# ✅ Base schema for User (Shared fields)
class UserBase(BaseModel):
    username: str
    email: EmailStr  # Ensures valid email format

# ✅ Schema for Creating a User (Request)
class UserCreate(UserBase):
    password: str  # Password required for user creation

# ✅ Schema for User Response (Excludes password)
class User(UserBase):
    user_id: int
    is_active: bool
    todos: List[Todo] = []  # User has multiple todos

    class Config:
        orm_mode = True
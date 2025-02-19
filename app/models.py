#this models are the pythonic representation of database tables

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,func,DateTime
from sqlalchemy.orm import relationship

#Base is used to define ORM models
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer,primary_key=True,index=True)
    username = Column(String(255),index=True,nullable=False)
    email = Column(String(255), unique=True, index=True,nullable=False)
    password=Column(String(225),nullable=False)
     # One-to-Many relationship (One User -> Many Todos)
    todos = relationship("Todo",back_populates="owner")
    is_active = Column(Boolean,default=False)



class Todo(Base):
    __tablename__ = "todos"
    todo_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True,nullable=False)
    description = Column(String(255), index=True,nullable=False)
    thumbnail=Column(String(225))
    #Timestamps for todos
    created_at = Column(DateTime, default=func.now())  # Set when a row is created
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Updates when modified
    #Due date and time for todos
    due_date_time=Column(DateTime,nullable=False)
    #Time to finish todo in min
    duration=Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.user_id"))
    # Many-to-One relationship (Each Todo belongs to one User)
    owner = relationship("User",back_populates="todos")

class SubTodo(Base):
    __tablename__ = "subtodos"
    subtodo_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True,nullable=False)
    description = Column(String(255), index=True,nullable=False)
    thumbnail=Column(String(225))
    #Timestamps for todos
    created_at = Column(DateTime, default=func.now())  # Set when a row is created
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # Updates when modified
    #duration in min 
    duration=Column(Integer,nullable=False) 
    owner_id = Column(Integer, ForeignKey("todos.todo_id"))
    # Many-to-One relationship (Each SubTodo belongs to one Todo)
    owner = relationship("Todo",back_populates="subtodos")
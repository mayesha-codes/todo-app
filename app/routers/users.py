from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db  # Ensure get_db is inside database.py


router = APIRouter()

# ✅ Route to Create a New User
@router.post("/users/", response_model=schemas.User)
def add_user(user:schemas.UserCreate, db:Session=Depends(get_db)):
    # Check if the email already exists
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    # Create and return the new user
    return crud.create_user(db=db,user=user)

# ✅ Route to Get all Users 
@router.get("/users/", response_model=list[schemas.User])
def get_users(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
    users = crud.get_users(db,skip=skip,limit=limit)
    return users

# ✅ Route to Get a User by ID
@router.get("/users/{user_id}/",response_model=schemas.User)
def get_user_by_id(user_id:int, db:Session=Depends(get_db)):
    db_user = crud.get_user_by_id(db,user_id =user_id )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


from .. import models, schemas
from fastapi import Depends, APIRouter
#from typing import List
from sqlalchemy.orm import Session
from ..database import *

router = APIRouter(
    prefix="/users",
    tags=["users"])




@router.get("/") #response_model=List[schemas.User])
def show_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

#testing getting data from the actual front end
@router.post("/")
def add_new_user(user: schemas.UserCreate, 
                 db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

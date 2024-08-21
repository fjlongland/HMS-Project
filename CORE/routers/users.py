from .. import models, schemas, utils
from fastapi import Depends, APIRouter, HTTPException, status, Response
from typing import List
from sqlalchemy.orm import Session
from ..database import *

router = APIRouter(
    prefix="/users",
    tags=["users"])



#Display all users in the database
@router.get("/", response_model=List[schemas.UserResponse])
def show_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

#Add new user to the database
@router.post("/", status_code=status.HTTP_201_CREATED, 
             response_model=schemas.UserResponse)
def add_new_user(user: schemas.UserCreate, 
                 db: Session = Depends(get_db)):
    
    user.password = utils.hash(user.password)

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

#Display filtered user according to id
@router.get("/{id}", response_model=schemas.UserResponse)
def get_one_user(id: int, 
                 db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    print(user.username)
    return user

#update a specific user
@router.put("/{id}", response_model=schemas.UserResponse)
def update_user(user: schemas.UserCreate, 
                id: int, 
                db: Session = Depends(get_db)):
    existing_user =db.query(models.User).filter(models.User.id == id)

    new_user = existing_user.first()

    if new_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no user with id: {id} exists.")
    
    existing_user.update(user.dict(),
                    synchronize_session=False)
    db.commit()

    return existing_user.first()

#Delete a specific user
@router.delete("/{id}")
def delete_user(id: int, 
                db: Session = Depends(get_db)):
    unwanted_user = db.query(models.User).filter(models.User.id == id)

    if unwanted_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no user with id: {id} exists.")
    
    unwanted_user.delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

from .. import models, schemas, utils, storage, oauth2
from fastapi import Depends, APIRouter, HTTPException, status, Response, Form
from typing import List
from sqlalchemy.orm import Session
from ..database import *

router = APIRouter(prefix="/users",
                   tags=["users"])


#Display all users in the database
@router.get("/", response_model=List[schemas.UserResponse])
def show_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

#Add new user to the database
@router.post("/", status_code=status.HTTP_201_CREATED, 
                response_model=schemas.UserResponse)
def add_new_user(username: str = Form(...),
                password: str = Form(...),
                user_email: str = Form(...),
                user_type: str = Form(...),
                db: Session = Depends(get_db)):
    
    hashed_password = utils.hash(password)

    new_user = models.User(username=username, password=hashed_password, user_email=user_email, user_type=user_type)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    storage.add_new_dir(str(new_user.user_id))

    return new_user

#Display filtered user according to id
@router.get("/{id}", response_model=schemas.UserResponse)
def get_one_user(id: int, 
                 db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_id == id).first()
    print(user.username)
    return user

#update a specific user
@router.put("/{id}", response_model=schemas.UserResponse)
def update_user(user: schemas.UserCreate, 
                id: int, 
                db: Session = Depends(get_db)):
    existing_user =db.query(models.User).filter(models.User.user_id == id)

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
    unwanted_user = db.query(models.User).filter(models.User.user_id == id).first()

    if unwanted_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no user with id: {id} exists.")
    
    db.delete(unwanted_user)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

#///////////////////////////////////////////////////////////////////////

@router.get("/type/")
def get_user_type(db: Session = Depends(get_db), 
                  current_user: int = Depends(oauth2.get_current_user) ):

    type = db.query(models.User.user_type).filter(models.User.user_id == current_user.user_id).first()

    return {"user_type": type[0]}

@router.post("/app_login")
def login(request: schemas.LoginRequest,
          db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    
    checkpassword = utils.hash(request.password)

    if user.password != checkpassword:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="incorrect password")
    
    return {"user_id": user.user_id, "user_type": user.user_type}
    
from .. import models, schemas
from fastapi import Depends, APIRouter, HTTPException, status, Response
from typing import List
from sqlalchemy.orm import Session
from ..database import *

router = APIRouter(prefix="/posts", 
                   tags=["posts"])
#get list of all posts
@router.get("/", response_model=List[schemas.PostResponse])
def show_all_posts(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()

    return posts

#create a new post
@router.post("/", response_model=schemas.PostResponse)
def create_new_post(post: schemas.PostCreate, 
                    db: Session = Depends(get_db)):

    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

##return specific post by id
@router.get("/{id}", response_model=schemas.PostResponse)
def get_one_post(id: int,
                 db: Session = Depends(get_db)):
    
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post.title)

    return post

#update a specific post
@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int,
                post: schemas.PostCreate,
                db: Session = Depends(get_db)):
    
    existing_post = db.query(models.Post).filter(models.Post.id == id)

    new_post = existing_post.first()

    if new_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} not found.")

    existing_post.update(post.dict(), 
                         synchronize_session=False)
    db.commit()

    return existing_post.first() 

#delete a specific post by id
@router.delete("/{id}")
def delete_post(id: int,
                db: Session = Depends(get_db)):
    
    unwanted_post = db.query(models.Post).filter(models.Post.id == id).first()

    if unwanted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no post with id:{id} exhists.")
    
    unwanted_post.delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

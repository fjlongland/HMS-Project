from .. import models, schemas, oauth2
from fastapi import Depends, APIRouter, HTTPException, status, Response, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.orm import Session
from ..database import *
import shutil
from pathlib import Path

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
                    db: Session = Depends(get_db),
                    current_user: int = Depends(oauth2.get_current_user)):

    new_post = models.Post(user_id_fk=current_user.user_id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

##return specific post by id
@router.get("/{id}", response_model=schemas.PostResponse)
def get_one_post(id: int,
                 db: Session = Depends(get_db)):
    
    post = db.query(models.Post).filter(models.Post.post_id == id).first()
    print(post.title)

    return post

#update a specific post
@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int,
                post: schemas.PostCreate,
                db: Session = Depends(get_db)):
    
    existing_post = db.query(models.Post).filter(models.Post.post_id == id)

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
    
    unwanted_post = db.query(models.Post).filter(models.Post.post_id == id).first()

    if unwanted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no post with id:{id} exhists.")
    
    db.delete(unwanted_post)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@router.post("/upload/")
async def upload_file_from_frontend(file: UploadFile = File(...), 
                                    current_user: int = Depends(oauth2.get_current_user),
                                    db: Session = Depends(get_db)):
    
    if not file.filename.endswith('.mp4'):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File must be of type .mp4")
    
    try:
        file_location = f"C:\\Users\\Admin\\Desktop\\HMS tets file destination\Destination\\{current_user.user_id}\\{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        new_post = models.Post(user_id_fk=current_user.user_id, title=file.filename, post_type="video", content="video", post_url=file_location)
        db.add(new_post)
        db.commit()

        return JSONResponse(content={"filename": file.filename})
    
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@router.get("/video/")
async def list_videos(db: Session = Depends(get_db), 
                      currnet_user: int = Depends(oauth2.get_current_user)):
    
    video_titles = db.query(models.Post.title).filter(models.Post.user_id_fk == currnet_user.user_id,
                                                      models.Post.post_type == "video").all()
    
    videos = [{"title": title[0]} for title in video_titles]

    return videos

    



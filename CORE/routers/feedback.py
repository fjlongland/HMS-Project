from .. import models, schemas, oauth2, utils
from fastapi import Depends, APIRouter, Form, HTTPException, status, Response, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
from sqlalchemy.orm import Session
from ..database import *
import shutil
from pathlib import Path

router = APIRouter(prefix = "/feedback",
                   tags = ["feedback"])

@router.get("/")
def get_all_feedback(db: Session = Depends(get_db)):
    feed = db.query(models.Feedback).all()

    return feed

@router.post("/")
def create_feedback(content: str = Form(...), 
                    post_id_fk: int = Form(...), 
                    currnemt_user: int = Depends(oauth2.get_current_user), 
                    db: Session = Depends(get_db)):
    
    new_feedback = models.Feedback(user_id_fk = currnemt_user.user_id, post_id_fk=post_id_fk, content=content)

    utils.logger.info(f"User: {currnemt_user.user_id}, posted feedback on post: {post_id_fk}")


    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)

    return new_feedback

@router.get("/display/{post_id}")
def display_feedback(post_id: str, 
                     db: Session = Depends(get_db)):

    feedback = db.query(models.Feedback.content).filter(models.Feedback.post_id_fk == post_id).first()

    utils.logger.info(f"feedback viewed by user")

    return {"content": feedback[0]}
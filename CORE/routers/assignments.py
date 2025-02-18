from .. import models, schemas, oauth2, utils
from fastapi import Depends, APIRouter, HTTPException, status, Response, Form, File, UploadFile, Query
from fastapi.responses import JSONResponse
#from typing import List
from sqlalchemy.orm import Session
from ..database import *
#import shutil
from pathlib import Path

router = APIRouter(prefix = "/assignment",
                   tags = ["assignments"])



@router.get("/")
def get_all_ass(db: Session = Depends(get_db)):
    assigns = db.query(models.Assignment).all()

    return assigns



@router.post("/")
def create_new_ass(title: str = Form(...),
                   content: str = Form(...),
                   #assign: schemas.AssignmentCreate,
                   db: Session = Depends(get_db),
                   current_user: int = Depends(oauth2.get_current_user)):
    new_ass = models.Assignment(user_id_fk=current_user.user_id, title=title, content=content)

    db.add(new_ass)
    db.commit()
    db.refresh(new_ass)

    utils.logger.info(f"User: {current_user.user_id} posted new assignment with title: {title}")

    return new_ass



@router.get("/{id}")
def get_one_assignment(id: int,
                       db: Session = Depends(get_db)):
    w_ass = db.query(models.Assignment).filter(models.Assignment.ass_id == id).first()

    return w_ass

@router.put("/{id}")
def update_assignment(id: int,
                      assign: schemas.AssignmentCreate,
                      db: Session = Depends(get_db)):
    old_ass = db.query(models.Assignment).filter(models.Assignment.ass_id == id)

    ass = old_ass.first()

    if ass == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post with id: {id} exhists!")
    old_ass.update(assign.dict(),
                   synchronize_session=False)
    db.commit()

    return old_ass.first()

@router.delete("/{id}")
def delete_assignment(id: int,
                      db: Session = Depends(get_db)):
    unwanted_assignment =  db.query(models.Assignment).filter(models.Assignment.ass_id == id).first()

    if unwanted_assignment == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No post with id: {id} exhists.")
    
    db.delete(unwanted_assignment)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

#/////////////////////////////////////////////////////////////////////\

@router.get("/list/")
def display_all_ass(db: Session = Depends(get_db)):
    try:
        assignments = db.query(models.Assignment.title).all()

        if not assignments:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="no assignments found")
        
        assignment_titles=[{"title": title[0]} for title in assignments]

        utils.logger.info("frontend request for list of assignments")

        return assignment_titles
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"an error occured: {str(e)}")
    

@router.get("/content/{title}")
def get_by_title(title: str, 
                 db: Session = Depends(get_db)):
    
    assignment = db.query(models.Assignment.ass_id, models.Assignment.content).filter(models.Assignment.title == title).first()

    utils.logger.info(f"webapp request for specific assignment: {title}")

    return {"ass_id": assignment[0], "content": assignment[1]}
    

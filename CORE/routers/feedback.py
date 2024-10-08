from .. import models, schemas, oauth2
from fastapi import Depends, APIRouter, HTTPException, status, Response, File, UploadFile
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
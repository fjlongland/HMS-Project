from .. import models, schemas
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["users"])




@router.get("/users", response_model=List[schemas.User])
def show_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

#testing getting data from the actual front end
@router.post("/")
async def test_recieve_input(user_input: schemas.User):
    print(f"username: {user_input.username}")
    print(f"password: {user_input.password}")
    return{"message": "Input recieved"}
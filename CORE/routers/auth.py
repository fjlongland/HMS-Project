from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(tags=["Authentication"])

@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    
    

    user = db.query(models.User).filter(models.User.username == user_credentials.username).first()
    
    utils.logger.info(f"login request from user: {user.username}, id: {user.user_id}")

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="invalid credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="invalid credentials")
    
    access_token = oauth2.create_access_token(data={"user_id": user.user_id})

    return {"token": access_token, 
            "token_type": "bearer"}


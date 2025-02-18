from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from . import schemas, database, models
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.secret_key
ALGORITHM = settings.token_algorythm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.token_exp_minutes

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id: str = payload.get("user_id")
   
        token_data = schemas.TokenData(user_id=user_id)

    except JWTError:
        raise credentials_exception
    
    return token_data


def get_current_user(token: str= Depends(oauth2_scheme), 
                     db: Session = Depends(database.get_db)):
    credentials_exeption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                         detail="could not validate user credentials",
                                         headers={"WWW-Authenticate": "Bearer"})
    
    token = verify_access_token(token, credentials_exeption)
    user = db.query(models.User).filter(models.User.user_id==token.user_id).first()
    return user
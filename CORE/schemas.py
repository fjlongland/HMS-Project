from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True  

class UserCreate(BaseModel):
    username: str
    password: str
    type: str

    class Config:
        orm_mode = True  

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True  

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Post(BaseModel):
    id: int

    class Config:
        orm_mode = True 

class PostCreate(BaseModel):
    title: str
    content: str
    post_type: str

    class Config:
        orm_mode = True 

class PostResponse(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True 

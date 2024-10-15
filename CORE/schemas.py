from pydantic import BaseModel
from typing import Optional
from fastapi import Form

class User(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True  

class UserCreate(BaseModel):
    username: str
    password: str 
    user_email: str 
    user_type: str 

    class Config:
        orm_mode = True  

class UserResponse(BaseModel):
    user_id: int
    username: str

    class Config:
        orm_mode = True  

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None

class Post(BaseModel):
    post_id: int

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


class AssignmentCreate(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    username: str
    password: str
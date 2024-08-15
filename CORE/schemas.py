from pydantic import BaseModel

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
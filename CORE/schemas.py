from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str

    class Config:
        orm_model = True

class UserCreate(BaseModel):
    username: str
    password: str
    type: str
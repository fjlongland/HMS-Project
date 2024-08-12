from pydantic import BaseModel


class TestInput(BaseModel):
    username: str
    password: str



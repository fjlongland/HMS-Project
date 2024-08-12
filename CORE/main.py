from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from . import database
from sqlalchemy.orm import Session
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

while True:
    try:
        conn = psycopg2.connect(host='localhost',
                                dbname='HMS_DB',
                                user='postgres',
                                password='4u2nV@5302P',
                                cursor_factory=RealDictCursor
                                )
        cursor = conn.cursor()
        print("connection successful")
        break

    except Exception as error:
        print("Connection failed")

#first API call for testing
@app.get("/")
async def root():
    return{"message:" "Hi There Traveler!"}

@app.get("/users")
def get_users(db: Session = Depends(database.get_db)):
    cursor.execute("""SELECT * FROM users""")
    users = cursor.fetchall()
    return users

class TestInput(BaseModel):
    input: str

@app.post("/test")
async def test_recieve_input(user_input: TestInput):
    print(f"user Input: {user_input.input}")
    return{"message": "Input recieved"}



#//////////////////USE THIS TO STARTUP THE APP/////////////////

#uvicorn CORE.main:app --reload

#//////////////////////////////////////////////////////////////

#TODO: decide if we need to use sqlalchemy or
#      if were just going to use normal sql

#TODO: look into what DB to use and 
#      make shure the cloud hosting works.

#TODO: build user table and finish
#      user registration and login.(Auth can be handled later)

#TODO: figer out what to do next.
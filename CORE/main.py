from fastapi import FastAPI#, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from . import database
#from sqlalchemy.orm import Session
from . import models

#init app
app = FastAPI()

#gives front and backend permission to send and recieve data
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

#first API call for testing
@app.get("/")
async def root():
    return{"message:" "Hi There Traveler!"}

@app.get("/users")
def get_users():    #db: Session = Depends(database.get_db)):
    database.cursor.execute("""SELECT * FROM users""")
    users = database.cursor.fetchall()
    return users


#testing getting data from the actual front end
@app.post("/test")
async def test_recieve_input(user_input: models.TestInput):
    print(f"user Input: {user_input.username, user_input.password}")
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
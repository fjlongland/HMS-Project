from fastapi import FastAPI#, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from . import database
#from sqlalchemy.orm import Session
from . import models
import unittest
from .routers import users, auth, posts
from .database import engine


if __name__=="__main__":
    unittest.main()

models.Base.metadata.create_all(bind=engine)

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




#/////////////ROUTERS/////////////////////////

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

#first API call for testing
@app.get("/")
async def root():
    return{"message:" "Hi There Traveler!"}

#//////////////////USE THIS TO STARTUP THE APP/////////////////

#uvicorn CORE.main:app --reload

#//////////////////////////////////////////////////////////////

#TODO change all sql to sqlalchemy

#TODO: look into what DB to use and 
#      make shure the cloud hosting works.

#TODO: build user table and finish
#      user registration and login.(Auth can be handled later)

#TODO: figer out what to do next.
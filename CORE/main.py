from fastapi import FastAPI#, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
#from . import database
#from sqlalchemy.orm import Session
from . import models
#import unittest
from .routers import users, auth, posts, assignments, feedback
from .database import engine
#from .config import settings
#import os
#import subprocess
from fastapi.staticfiles import StaticFiles

#http://127.0.0.1:8000/docs
#if __name__=="__main__":
    #subprocess.run(["uvicorn", "CORE.main:app", "--reload"])

models.Base.metadata.create_all(bind=engine)

#init app
app = FastAPI()

app.mount("/videos", StaticFiles(directory="C:/Users/Admin/Desktop/HMS tets file destination/Destination"), name="videos")

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
app.include_router(assignments.router)
app.include_router(feedback.router)

#first API call for testing
@app.get("/")
async def root():
    return{"message": "Hi There Traveler!"}

#//////////////////USE THIS TO STARTUP THE APP/////////////////

#uvicorn CORE.main:app --reload

#//////////////////////////////////////////////////////////////


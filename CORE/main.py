from fastapi import FastAPI, Depends
from . import database
from sqlalchemy.orm import Session
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

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





#//////////////////USE THIS TO STARTUP THE APP/////////////////

#uvicorn CORE.main:app --reload

#//////////////////////////////////////////////////////////////

#TODO: look into what DB to use and 
#make shure the cloud hosting works.

#TODO: build user table and finish
# user registration and login.(Auth can be handled later)

#TODO: figer out what to do next.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse
import psycopg2
from psycopg2.extras import RealDictCursor



#we need to decide if we are going to use this or if we are just going to user SQL
password = "4u2nV@5302P"
encoded_password = urllib.parse.quote_plus(password)

DB_URL = f"postgresql://postgres:{encoded_password}@localhost/HMS_DB"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(#autocommmit=False,
                            autoflush=False,
                            bind=engine)

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Database connection
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
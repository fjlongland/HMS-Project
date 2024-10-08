from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings



#we need to decide if we are going to use this or if we are just going to user SQL
password = settings.db_password
encoded_password = urllib.parse.quote_plus(password)

#connection string in the form of postgesql://(username):(password)@(hostname):(database port)/(database name)
DB_URL = f"postgresql://{settings.db_username}:{encoded_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}"

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


#////////////////////////////Database connection when not using SQLalchemy//////////////////////////////////////
#Database connection
#while True:
 #   try:
 #       conn = psycopg2.connect(host='localhost',
 #                               dbname='HMS_DB',
 #                               user='postgres',
 #                               password='4u2nV@5302P',
 #                               cursor_factory=RealDictCursor
 #                               )
 #       cursor = conn.cursor()
 #       print("connection successful")
 #       break
 #
 #   except Exception as error:
 #       print("Connection failed")
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse

password = "4u2nV@5302P"
encoded_password = urllib.parse.quote_plus(password)

DB_URL = f"postgresql://postgres:{encoded_password}@localhost/HMS_DB"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommmit=False,
                            autoflush=False,
                            bind=engine)

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__="posts"

    id = Column(Integer, primary_key=True, nullable=False)
    post_type = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id_fk = Column(Integer, ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    owner = relationship("User")

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    type = Column(String, nullable=False)

    


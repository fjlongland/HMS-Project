from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__="users"

    user_id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    user_email = Column(String, nullable=False)
    user_type = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


    
class Post(Base):
    __tablename__="posts"

    post_id = Column(Integer, primary_key=True, nullable=False)
    user_id_fk = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    ass_id_fk = Column(Integer, ForeignKey("assignments.ass_id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    post_type = Column(String, nullable=False)
    content = Column(String, nullable=False)
    post_url = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner = relationship("User")
    owner = relationship("Assignment")


class Assignment(Base):
    __tablename__="assignments"

    ass_id = Column(Integer, primary_key=True, nullable=False)
    user_id_fk = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner = relationship("User")


class Feedback(Base):
    __tablename__="feedback"

    feedback_id = Column(Integer, primary_key=True, nullable=False)
    user_id_fk = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    post_id_fk = Column(Integer, ForeignKey("posts.post_id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner = relationship("User")
    owner = relationship("Post")
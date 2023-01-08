import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.sql.sqltypes import Enum

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Enum


Base = declarative_base()

class Follower:
    __tablename__ = 'Followers'
    user_from_id = Column(Integer, ForeignKey('Users.id'))
    user_to_id = Column(Integer, ForeignKey('Users.id'))

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)  # Set primary key
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)

class Post(Base):
    __tablename__ = 'Post'
    ID = Column(Integer, primary_key=True) # Add primary key
    user_id = Column(Integer, ForeignKey('Users.id'))

class Comment(Base):
    __tablename__ = 'Comment'
    ID = Column(Integer, primary_key=True)  # Add primary key
    post_id = Column(Integer, ForeignKey('Post.ID'))
    author_id = Column(Integer, ForeignKey('Users.id'))
    comment_text = Column(String)

class Media(Base):
    __tablename__ = 'Media'
    ID = Column(Integer, primary_key=True)
    type = Enum('active', 'inactive', 'pending')
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.ID'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

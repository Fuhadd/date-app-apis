from cgitb import text
from codecs import getencoder
from email.policy import default
from http import server
from sqlite3 import Timestamp
from time import timezone
from typing import List, Type
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship
#from sqlalchemy_utils import URLType

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    username = Column(String, nullable=False, server_default='user')
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    gender = Column(String, nullable=False, server_default='male')
    age = Column(String, nullable=False, server_default='age')
    

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default='now()')
    #is_active = Column(Boolean, default=True,nullable=False)

   # items = relationship("Item", back_populates="owner")


class Images(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True, nullable=False)

    image_url = Column(String, nullable=False)

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default='now()')

    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"))

    owner = relationship("User")
    
    
class Interest(Base):
    __tablename__ = "interest"
    id = Column(Integer, primary_key=True, index=True, nullable=False)

    interests = Column(ARRAY(String), nullable=False, server_default=None)

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default='now()')

    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"))

    owner = relationship("User")

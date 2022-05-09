from cgitb import text
from email.policy import default
from http import server
from sqlite3 import Timestamp
from time import timezone
from typing import List, Type
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    interests = Column(ARRAY(String), nullable=False, server_default=None)
    url = Column(ARRAY(URLType))
    #image_url = Column(ARRAY(URLType))

    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default='now()')
    #is_active = Column(Boolean, default=True,nullable=False)

   # items = relationship("Item", back_populates="owner")

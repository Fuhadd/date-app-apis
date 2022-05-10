from pydantic import BaseModel, EmailStr
from typing import  Optional
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    #interests: list
    username:str
    gender:str
    age:str
    
    

    class Config:
        orm_mode = True

    
class UserDetails (UserCreate):
    created_at: datetime
    id:int
    
    class Config:
        orm_mode = True
    

class user_error(BaseModel):
    email: Optional[str]
    interests: list
    
    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: Optional[str] = None
    
class Token(BaseModel):
    access_token: str
    token_type: str

class UserImageUpload(BaseModel):
    owner_id: str
    image_url:str
    class Config:
        orm_mode = True

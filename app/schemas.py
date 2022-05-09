from pydantic import BaseModel, EmailStr
from typing import  Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    interests: list
    
    username:str
    class Config:
        orm_mode = True
    
class UserDetails (UserCreate):
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



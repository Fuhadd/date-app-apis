
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException

from sqlalchemy.orm import Session

from app import oauth2, utils, database

from .. import schemas, models


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.user_error)
async def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):

    hashed_password = utils.hash(user.password)

    user.password = hashed_password

    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/', response_model=List[schemas.UserDetails])
def get_users(user=schemas.UserDetails, db: Session = Depends(database.get_db),current_user: int = Depends(oauth2.get_current_user)):
    users=db.query(models.User).all()
    return users

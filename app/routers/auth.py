from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import database, models, schemas, utils, oauth2


router = APIRouter(
    tags=["Authetication"]
)


@router.post("/login")
def login(user_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    print("jfjfj")

    user = db.query(models.User).filter(
        models.User.email == user_credential.username).first()

    print(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    print(user.id)

    if not utils.verify(user_credential.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return access_token

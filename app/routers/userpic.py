import shutil
# import cloudinary
# import cloudinary.uploader
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException,File, UploadFile


from sqlalchemy.orm import Session

from app import oauth2, utils, database

from .. import schemas, models


router = APIRouter(
   
    tags=['user']
)

@router.post('user/test' )
def get_users(db: Session = Depends(database.get_db),current_user: int = Depends(oauth2.get_current_user),uploaded_file: UploadFile = File(...)):
    
    user=db.query(models.User).filter(models.User.id == current_user.id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    file_location = f"media/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(uploaded_file.file, file_object)  
    
    # result = cloudinary.uploader.upload(uploaded_file.file)
    # url = result.get("url")  
    
        
    
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}
    
 
#  @app.post("/posts/",status_code=status.HTTP_201_CREATED)
# def create_post(
#     title:str,body:str,file: UploadFile = File(...), db: Session = Depends(get_db),current_user: models.User = Depends(get_current_user)
# ):
#     user_id=current_user.id

#     result = cloudinary.uploader.upload(file.file)
#     url = result.get("url")

#     return crud.create_post(db=db,user_id=user_id,title=title,body=body,url=url)


# def create_post(db: Session,user_id:int,title:str,body:str,url:str):
#     db_post = models.Post(title=title,body=body,owner_id=user_id,url=url)
#     db.add(db_post)
#     db.commit()
#     db.refresh(db_post)
#     return db_post
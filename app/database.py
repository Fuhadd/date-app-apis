import time
import psycopg2
import cloudinary
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# password = 'indomitables123'
# user_name = 'postges'
# host = 'localhost'
# db_name = 'dateapp'
# SQLALCHEMY_DATABASE_URL =  f"postgresql://{user_name}:{password}@{host}:5433/{db_name}"

cloudinary.config( 
  cloud_name = "aminu", 
  api_key = "636974665241245", 
  api_secret = "KJCHz6yfwnv_SmcsMZZ6HDaqdnc" 
)

password = 'c8cf18ef002f10d1cea210d3925b653bacd79dd2643f44677a01e345451612c0'
user_name = 'pjjwomzqmgrmsq'
host = 'ec2-44-196-223-128.compute-1.amazonaws.com'
db_name = 'd9p5qd0d2pit25'
SQLALCHEMY_DATABASE_URL =  f"postgresql://{user_name}:{password}@{host}/{db_name}"



engine = create_engine(
    f"postgresql://{user_name}:{password}@{host}/{db_name}"
    #f"postgresql://{user_name}:{password}@{host}:5433/{db_name}
    # f"postgresql://postgres:indomitables123@localhost/dateapp"
    # SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='dateapp', user='postgres',
#                                 password='indomitables123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)

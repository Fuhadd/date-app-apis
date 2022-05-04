import time
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

password = 'indomitables123'
SQLALCHEMY_DATABASE_URL =  f"postgresql://postges:{password}@localhost:5433/datingapi"


engine = create_engine(
    f"postgresql://postgres:indomitables123@localhost/dateapp"
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
        
        
while True:

    try:
        conn = psycopg2.connect(host='localhost', database='dateapp', user='postgres',
                                password='indomitables123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

import os

# import psycopg2
from dotenv import load_dotenv

# from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import time


load_dotenv()

db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# For reference only 👇🏻
# while True:
#     try:
#         conn = psycopg2.connect(
#             host=db_host,
#             port=db_port,
#             database=db_name,
#             user=db_user,
#             password=db_pass,
#             cursor_factory=RealDictCursor,
#         )
#         cursor = conn.cursor()
#         print("Successfully connected to the database")
#         break
#     except Exception as error:
#         print("Failed to connect to database")
#         print("Error: ", error)
#         time.sleep(4)

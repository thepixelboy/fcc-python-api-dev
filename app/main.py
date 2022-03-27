import os
import time

import psycopg2
from dotenv import load_dotenv
from fastapi import FastAPI
from psycopg2.extras import RealDictCursor

from . import models
from .database import engine
from .routers import auth, post, user

load_dotenv()

db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")


models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)


while True:
    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_pass,
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("Successfully connected to the database")
        break
    except Exception as error:
        print("Failed to connect to database")
        print("Error: ", error)
        time.sleep(4)


@app.get("/")
async def root():
    return {"message": "Welcome to my API"}


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv(r"D:\Programming\FastAPI\.env")

# We would use cloud postgres instead of local postgres

POSTGRES_DATABASE_URL = os.getenv("POSTGRES_DATABASE_URL")

engine = create_engine(
    POSTGRES_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

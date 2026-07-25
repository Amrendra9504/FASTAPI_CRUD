import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

username = "root"
password = "root"
host = "127.0.0.1"
port = "3306"
database_name = "fastapidemo"

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}"
DB_URL = os.getenv("DATABASE_URL", DATABASE_URL)

engine = create_engine(DB_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, bind=engine)
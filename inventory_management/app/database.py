from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://library_project_sit722_user:SmD7HpghUvtlyEjW3z5t7PSGBGHLBeO0@dpg-crf9fc2j1k6c73dj2od0-a.oregon-postgres.render.com/library_project_sit722" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

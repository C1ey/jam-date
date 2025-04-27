# app/config.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration."""
    SECRET_KEY = os.getenv("SECRET_KEY", "Som3$ec5etK*y")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///jamdate.db"
    ).replace("postgres://", "postgresql://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "a-super-secret-key")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 'sqlite:///jamdate.db'
    ).replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'a-super-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')

    #IF EXPIRES

    """# Log in again
RAW=$(curl -s -X POST http://127.0.0.1:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"secret123"}')

# Extract the new token
TOKEN=$(echo $RAW | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")
"""
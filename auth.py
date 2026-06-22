# auth.py

from jose import jwt

SECRET_KEY="mysecretkey"

ALGORITHM="HS256"

def create_access_token(data:dict):
    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
from datetime import datetime, timezone, timedelta
from typing import Optional

from passlib.context import CryptContext
from jose import jwt

SECRET_KEY = ""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

def hash_password(raw_password:str)-> str:
    return pwd_context.hash(raw_password)


def verify_password(raw_password:str, hashed_password:str)->bool:
    return pwd_context.verify(raw_password, hashed_password)

def create_access_token(
        sub:str,
        role:str,
        expired_minutes:int = ACCESS_TOKEN_EXPIRE_MINUTES
)->str:
    now = datetime.now(timezone.utc)
    payload = {
        'sub': sub,
        'role': role,
        'exp': now + timedelta(minutes=expired_minutes)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token:str)->Optional[dict]:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

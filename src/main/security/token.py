import os
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

SECRET_KEY= os.getenv("JWT_SECRET")
ALGORITHM= os.getenv("JWT_ALGORITHM")

def gerar_jwt(user_id: str):
    payload = {
        "sub": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=60)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verificar_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        return None

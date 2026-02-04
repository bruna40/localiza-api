# models/user_delete_dto.py
from pydantic import BaseModel

class UserDeleteDTO(BaseModel):
    password: str

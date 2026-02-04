from pydantic import BaseModel
from typing import Optional

class UserUpdateNameDTO(BaseModel):
    name: str
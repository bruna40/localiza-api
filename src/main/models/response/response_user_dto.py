from datetime import datetime
from pydantic import BaseModel

class UserResponseDTO(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

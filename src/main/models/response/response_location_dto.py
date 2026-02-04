from pydantic import BaseModel
from typing import Optional

class LocationResponse(BaseModel):
    status: str
    place: Optional[str] = None
    type: Optional[str] = None

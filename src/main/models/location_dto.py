from pydantic import BaseModel

class LocationDTO(BaseModel):
    user_id: str
    latitude: float
    longitude: float

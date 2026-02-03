from fastapi import APIRouter, HTTPException
from src.main.models.location_dto import LocationDTO
from src.main.service.process_service import process_location

router = APIRouter(
    prefix="/location",
    tags=["Location"]
)

@router.post("/check")
def check_location(data: LocationDTO):
    try:
        result = process_location(data)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Erro ao processar localização"
        )

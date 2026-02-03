from fastapi import APIRouter, HTTPException
from src.main.models.login_dto import LoginDTO, TokenResponse
from src.main.models.user import UserCreate, UserResponse
from src.main.service.user_service import create, login 

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/create-user", response_model=UserResponse)
def create_user(user: UserCreate):
    try:
        return create(user.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.post("/login", response_model=TokenResponse)
def login_user(user: LoginDTO):
    try:
        return login(user.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

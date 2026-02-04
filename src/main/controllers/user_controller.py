from fastapi import APIRouter, HTTPException, Depends
from src.main.security.token import get_current_user_id
from src.main.models.login_dto import LoginDTO, TokenResponse
from src.main.models.user import UserCreate, UserResponse
from src.main.service.user_service import create, login, get_user 

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
    
@router.get("")
def user_detail(user_id: str = Depends(get_current_user_id)):
    try: 
        return get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

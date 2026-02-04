from fastapi import APIRouter, HTTPException, Depends
from src.main.models.response.response_delete_user_dto import UserDeleteDTO
from src.main.models.user_update_name_dto import UserUpdateNameDTO
from src.main.security.token import get_current_user_id
from src.main.models.login_dto import LoginDTO
from src.main.models.user import UserCreate
from src.main.service.user_service import create, delete_account, login, get_user, update_name 

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

def create_user(user: UserCreate):
    try:
        return create(user.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



def login_user(user: LoginDTO):
    try:
        return login(user.model_dump())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


def user_detail(user_id: str = Depends(get_current_user_id)):
    try: 
        return get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


def update_user(
    body: UserUpdateNameDTO,
    user_id: str = Depends(get_current_user_id)
):
    try:
        return update_name(user_id, body.name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



def delete_user(
    body: UserDeleteDTO,
    user_id: str = Depends(get_current_user_id)
):
    try:
        delete_account(user_id, body.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

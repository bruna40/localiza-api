from fastapi import APIRouter, Depends
from src.main.controllers.user_controller import (
    create_user,
    login_user,
    user_detail,
    update_user,
    delete_user
)
from src.main.security.token import get_current_user_id

router = APIRouter(prefix="/users", tags=["Users"])

router.post("/create-user")(create_user)
router.post("/login")(login_user)

router.get("")(user_detail)
router.put("/update-name")(update_user)
router.delete("")(delete_user)

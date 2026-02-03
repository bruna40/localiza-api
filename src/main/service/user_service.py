from src.main.repositories.user_repository import create_user, find_user_by_email
from src.main.security.password import hash_password, verify_password
from src.main.security.token import gerar_jwt

def create(user: dict):
    if find_user_by_email(user["email"]):
        raise ValueError("Email já cadastrado")

    user["password"] = hash_password(user["password"])
    user_id, created_at = create_user(user)

    return {
        "id": str(user_id),
        "name": user["name"],
        "email": user["email"],
        "created_at": created_at
    }
    
def login(user: dict):
    existing_user = find_user_by_email(user["email"])
    if not existing_user:
        return "Usuario não encontrado"

    if not verify_password(user["password"], existing_user["password"]):
        return "Credenciais inválidas"
    
    token = gerar_jwt(str(existing_user["_id"]))
    return {
        "acess_token": token,
        "token_type": "bearer"
    }

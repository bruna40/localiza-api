from src.main.validators.user_validator import validate_email, validate_password, normalize_name, normalize_email
from src.main.repositories.user_repository import create_user, soft_delete_user,  find_user_by_email, find_by_user_id, update_user_name
from src.main.security.password import hash_password, verify_password
from src.main.security.token import gerar_jwt


def create(user: dict):
    validate_email(user["email"])
    user["email"] = normalize_email(user["email"])
    if find_user_by_email(user["email"]):
        raise ValueError("Email já cadastrado")

    user["name"] = normalize_name(user["name"])


    validate_password(user["password"])


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

def get_user(user_id: str):
    
    user = find_by_user_id(user_id)
    if not user:
        raise ValueError("Usuário não encontrado")
    
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "created_at": user["created_at"]
    }
    
def update_name(user_id: str, name: str):
    name_updated = normalize_name(name)

    user = update_user_name(user_id, name_updated)

    return {
        "id": str(user["id"]),
        "name": user["name"],
        "email": user["email"],
        "created_at": user["created_at"]
    }

    
def delete_account(user_id: str, password: str):
    user = find_by_user_id(user_id)

    if not user:
        raise ValueError("Usuário não encontrado")

    if not verify_password(password, user["password"]):
        raise ValueError("Senha incorreta")

    soft_delete_user(user_id)

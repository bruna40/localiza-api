import re

def normalize_name(name: str) -> str:
    return name.strip().lower()

def validate_password(password: str) -> str:
    if len(password) < 6:
        raise ValueError("Senha deve ter no mínimo 6 caracteres")

    if not re.search(r"[A-Za-z]", password):
        raise ValueError("Senha precisa ter pelo menos uma letra")

    if not re.search(r"\d", password):
        raise ValueError("Senha precisa ter pelo menos um número")


def validate_email(email: str) -> str:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        raise ValueError("Email inválido")

def normalize_email(email: str) -> str:
    return email.strip().lower()
from pydantic import BaseModel

class TokenResponse(BaseModel):
    acess_token: str
    token_type: str
    
class LoginDTO(BaseModel):
    email: str
    password: str

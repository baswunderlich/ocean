from pydantic import BaseModel

class Login (BaseModel):
    password: str
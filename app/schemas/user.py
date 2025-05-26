from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    nombre: str
    rol: Optional[str] = "user"

class UserCreate(UserBase):
    contraseña: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    nombre: str
    contraseña: str
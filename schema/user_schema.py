from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    phone: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None

class UserResponse(UserCreate):
    id: int    
 

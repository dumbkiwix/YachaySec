from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    phone: str

class UserResponse(UserCreate):
    id: int    
 

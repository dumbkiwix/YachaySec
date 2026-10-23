from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int]
    name: str
    phone: str

class UserResponse(UserCreate):
    id: int    

from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime
from pydantic import Field

class UserCreate(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50
    )
    email: EmailStr
    password: str = Field(
        min_length=8
    )

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

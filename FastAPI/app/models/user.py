from typing import Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    user_id: int
    username: str
    email: str
    password: str 
    phone_number: Optional[str] = None
    profile_picture: Optional[str] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "user_id": 1,
                "username": "johndoe",
                "email": "johndoe@example.com",
                "phone_number": "+1234567890",
                "profile_picture": "http://example.com/avatar.jpg"
            }
        }
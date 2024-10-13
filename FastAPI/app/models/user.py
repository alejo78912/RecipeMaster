from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    """
    Pydantic model representing a user in the system.
    """
    id: int
    username: str
    email: str
    password: str
    phone_number: str
    profile_picture: Optional[str]
    creation_date: str
    update_date: str

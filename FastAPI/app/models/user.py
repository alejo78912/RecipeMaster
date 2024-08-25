from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str
    email: str
    password: str
    phone_number: str
    profile_picture: str
    
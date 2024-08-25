from pydantic import BaseModel


class GroupMember(BaseModel):
    group_id: int
    user_id: int
    role: str
    
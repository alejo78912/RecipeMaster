from pydantic import BaseModel


class Group(BaseModel):
    group_id: int
    name: str
    description: str
    
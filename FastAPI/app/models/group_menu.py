from pydantic import BaseModel

class GroupMenu(BaseModel):
    group_id: int
    menu_id: int
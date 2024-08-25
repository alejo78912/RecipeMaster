import datetime
from pydantic import BaseModel

class Menu(BaseModel):
    menu_id: int
    group_id: int
    name: str
    total_calories: float
    start_date: datetime
    end_date: datetime
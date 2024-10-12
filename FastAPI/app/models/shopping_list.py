import datetime
from pydantic import BaseModel

class ShoppingList(BaseModel):
    list_id: int
    group_id: int
    created_date: datetime
    is_purchased: bool
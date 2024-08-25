import datetime
from pydantic import BaseModel

class PantryItem(BaseModel):
    pantry_id: int
    ingredient_id: int
    quantity: float
    unit_id: int
    expiry_date: datetime
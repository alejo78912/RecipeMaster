from pydantic import BaseModel

class ShoppingListItem(BaseModel):
    list_id: int
    ingredient_id: int
    quantity: float
    unit_id: int
    
import datetime
from pydantic import BaseModel

class MenuRecipe(BaseModel):
    menu_id: int
    recipe_id: int
    date: datetime
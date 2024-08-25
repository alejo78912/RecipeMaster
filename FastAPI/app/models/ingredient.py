from pydantic import BaseModel


class Ingredient(BaseModel):
    ingredient_id: int
    name: str
    category_id: int
    state_id: int
    calorie_unit_id: int
    calories_per_unit: float
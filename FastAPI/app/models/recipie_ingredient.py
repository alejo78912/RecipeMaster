from pydantic import BaseModel


class RecipeIngredient(BaseModel):
    recipe_id: int
    ingredient_id: int
    quantity: float
    unit_id: int
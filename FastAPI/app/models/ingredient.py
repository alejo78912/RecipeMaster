"""
Pydantic models for the Ingredient entity.
"""

from pydantic import BaseModel


class Ingredient(BaseModel):
    """
    Pydantic model representing an ingredient.

    Attributes:
        ingredient_id (int): The unique identifier for the ingredient.
        name (str): The name of the ingredient.
        category_id (int): The ID of the category this ingredient belongs to.
        state_id (int): The ID of the state (e.g., solid, liquid) of the ingredient.
        calorie_unit_id (int): The ID of the unit used to measure calories for the ingredient.
        calories_per_unit (float): The number of calories per unit of the ingredient.
    """
    ingredient_id: int
    name: str
    category_id: int
    state_id: int
    calorie_unit_id: int
    calories_per_unit: float
    
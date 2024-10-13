"""
Pydantic models for the RecipeIngredient entity.
"""

from pydantic import BaseModel


class RecipeIngredient(BaseModel):
    """
    Pydantic model representing the relationship between a recipe and its ingredients.

    Attributes:
        recipe_id (int): The ID of the recipe.
        ingredient_id (int): The ID of the ingredient used in the recipe.
        quantity (float): The quantity of the ingredient used.
        unit_id (int): The ID of the unit used to measure the quantity.
    """
    recipe_id: int
    ingredient_id: int
    quantity: float
    unit_id: int
    
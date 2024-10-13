"""
Pydantic models for the RecipeCategoryBridge entity.
"""

from pydantic import BaseModel


class RecipeCategoryBridge(BaseModel):
    """
    Pydantic model representing the relationship between a recipe and a category.

    Attributes:
        recipe_id (int): The ID of the recipe.
        category_id (int): The ID of the category the recipe belongs to.
    """
    recipe_id: int
    category_id: int
    
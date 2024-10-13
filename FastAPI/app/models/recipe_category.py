"""
Pydantic models for the RecipeCategory entity.
"""

from pydantic import BaseModel


class RecipeCategory(BaseModel):
    """
    Pydantic model representing a category for recipes.

    Attributes:
        category_id (int): The unique identifier for the recipe category.
        name (str): The name of the recipe category.
        description (str): A description of the recipe category.
    """
    category_id: int
    name: str
    description: str
    
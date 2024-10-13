"""
Pydantic models for the Category entity.
"""

from pydantic import BaseModel


class Category(BaseModel):
    """
    Pydantic model representing a category for ingredients or recipes.

    Attributes:
        category_id (int): The unique identifier for the category.
        name (str): The name of the category.
        description (str): A brief description of the category.
    """
    category_id: int
    name: str
    description: str
    
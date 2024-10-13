"""
Pydantic models for the MenuRecipe entity.
"""

from datetime import datetime  # Using datetime for date
from pydantic import BaseModel


class MenuRecipe(BaseModel):
    """
    Pydantic model representing the relationship between a menu and a recipe.

    Attributes:
        menu_id (int): The ID of the menu.
        recipe_id (int): The ID of the recipe.
        date (datetime): The date and time the recipe was added to the menu.
    """
    menu_id: int
    recipe_id: int
    date: datetime  # Using datetime for timestamp
    
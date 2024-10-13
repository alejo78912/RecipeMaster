"""
Pydantic models for the Recipe entity.
"""

from pydantic import BaseModel


class Recipe(BaseModel):
    """
    Pydantic model representing a recipe.

    Attributes:
        recipe_id (int): The unique identifier for the recipe.
        title (str): The title of the recipe.
        description (str): A brief description of the recipe.
        instructions (str): The step-by-step instructions for the recipe.
        cooking_time (int): The time it takes to cook the recipe.
        difficulty (str): The difficulty level of the recipe.
        is_public (bool): A flag indicating whether the recipe is public.
        total_calories (float): The total number of calories in the recipe.
        group_id (int): The ID of the group the recipe belongs to.
        time_unit_id (int): The ID of the time unit associated with the cooking time.
    """
    recipe_id: int
    title: str
    description: str
    instructions: str
    cooking_time: int
    difficulty: str
    is_public: bool
    total_calories: float
    group_id: int
    time_unit_id: int
    
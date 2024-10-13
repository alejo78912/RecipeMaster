"""
Pydantic models for the IngredientAPI entity.
"""

from pydantic import BaseModel


class IngredientAPI(BaseModel):
    """
    Pydantic model representing the relationship between an ingredient and an external API.

    Attributes:
        ingredient_id (int): The unique identifier for the ingredient.
        api_id (str): The identifier for the external API associated with the ingredient.
    """
    ingredient_id: int
    api_id: str
    
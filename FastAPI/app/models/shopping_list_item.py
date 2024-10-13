"""
Pydantic models for the ShoppingListItem entity.
"""

from pydantic import BaseModel


class ShoppingListItem(BaseModel):
    """
    Pydantic model representing an item in a shopping list.

    Attributes:
        list_id (int): The ID of the shopping list.
        ingredient_id (int): The ID of the ingredient in the shopping list item.
        quantity (float): The quantity of the ingredient.
        unit_id (int): The unit of measurement for the quantity.
    """
    list_id: int
    ingredient_id: int
    quantity: float
    unit_id: int
    
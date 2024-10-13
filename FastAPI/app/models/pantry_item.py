"""
Pydantic models for the PantryItem entity.
"""

from datetime import date  # Import the correct type
from pydantic import BaseModel


class PantryItem(BaseModel):
    """
    Pydantic model representing an item in the pantry.

    Attributes:
        pantry_id (int): The ID of the pantry.
        ingredient_id (int): The ID of the ingredient.
        quantity (float): The quantity of the ingredient.
        unit_id (int): The unit ID for the quantity measurement.
        expiry_date (date): The expiry date of the item.
    """
    pantry_id: int
    ingredient_id: int
    quantity: float
    unit_id: int
    expiry_date: date  # Changed from `datetime` to `date`
    
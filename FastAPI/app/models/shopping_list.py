"""
Pydantic models for the ShoppingList entity.
"""

from datetime import datetime  # Use datetime.datetime or datetime.date depending on usage
from pydantic import BaseModel


class ShoppingList(BaseModel):
    """
    Pydantic model representing a shopping list.

    Attributes:
        list_id (int): The unique identifier for the shopping list.
        group_id (int): The ID of the group the shopping list is associated with.
        created_date (datetime): The date the shopping list was created.
        is_purchased (bool): A flag indicating whether the shopping list has been purchased.
    """
    list_id: int
    group_id: int
    created_date: datetime
    is_purchased: bool
    
"""
Pydantic models for the Menu entity.
"""

from datetime import datetime  # Use datetime for start_date and end_date fields
from pydantic import BaseModel


class Menu(BaseModel):
    """
    Pydantic model representing a menu.

    Attributes:
        menu_id (int): The unique identifier for the menu.
        group_id (int): The ID of the group the menu is associated with.
        name (str): The name of the menu.
        total_calories (float): The total calories of the menu.
        start_date (datetime): The start date of the menu.
        end_date (datetime): The end date of the menu.
    """
    menu_id: int
    group_id: int
    name: str
    total_calories: float
    start_date: datetime
    end_date: datetime
    
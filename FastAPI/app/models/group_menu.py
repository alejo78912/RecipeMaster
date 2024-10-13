"""
Pydantic models for the GroupMenu entity.
"""

from pydantic import BaseModel


class GroupMenu(BaseModel):
    """
    Pydantic model representing the relationship between a group and a menu.

    Attributes:
        group_id (int): The ID of the group.
        menu_id (int): The ID of the menu associated with the group.
    """
    group_id: int
    menu_id: int
    
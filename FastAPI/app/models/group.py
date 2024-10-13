"""
Pydantic models for the Group entity.
"""

from pydantic import BaseModel


class Group(BaseModel):
    """
    Pydantic model representing a group.

    Attributes:
        group_id (int): The unique identifier for the group.
        name (str): The name of the group.
        description (str): A description of the group.
    """
    group_id: int
    name: str
    description: str
    
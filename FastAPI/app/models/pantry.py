"""
Pydantic models for the Pantry entity.
"""

from pydantic import BaseModel


class Pantry(BaseModel):
    """
    Pydantic model representing a pantry for a group.

    Attributes:
        pantry_id (int): The unique identifier for the pantry.
        group_id (int): The ID of the group associated with the pantry.
    """
    pantry_id: int
    group_id: int
    
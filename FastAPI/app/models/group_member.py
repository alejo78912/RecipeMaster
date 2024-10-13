"""
Pydantic models for the GroupMember entity.
"""

from pydantic import BaseModel


class GroupMember(BaseModel):
    """
    Pydantic model representing the relationship between a group and a user.

    Attributes:
        group_id (int): The ID of the group.
        user_id (int): The ID of the user.
        role (str): The role of the user within the group.
    """
    group_id: int
    user_id: int
    role: str
    
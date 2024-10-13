"""
Pydantic models for the State entity.
"""

from pydantic import BaseModel


class State(BaseModel):
    """
    Pydantic model representing the state of an ingredient or item.

    Attributes:
        state_id (int): Unique identifier for the state.
        name (str): Name of the state.
        description (str): Description of the state.
    """
    state_id: int
    name: str
    description: str
    
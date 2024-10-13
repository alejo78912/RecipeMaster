"""
Pydantic models for the TimeUnit entity.
"""

from pydantic import BaseModel


class TimeUnit(BaseModel):
    """
    Pydantic model representing a time unit.

    Attributes:
        time_unit_id (int): The unique identifier for the time unit.
        name (str): The name of the time unit.
        abbreviation (str): The abbreviation of the time unit.
    """
    time_unit_id: int
    name: str
    abbreviation: str
    
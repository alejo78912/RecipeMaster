"""
Pydantic models for the Unit entity.
"""

from pydantic import BaseModel


class Unit(BaseModel):
    """
    Pydantic model representing a unit of measurement.

    Attributes:
        unit_id (int): The unique identifier for the unit.
        name (str): The name of the unit.
        abbreviation (str): The abbreviation of the unit.
    """
    unit_id: int
    name: str
    abbreviation: str
    
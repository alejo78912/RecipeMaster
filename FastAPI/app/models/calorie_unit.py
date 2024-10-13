"""
Pydantic models for the CalorieUnit entity.
"""

from pydantic import BaseModel


class CalorieUnit(BaseModel):
    """
    Pydantic model representing a unit for measuring calories.

    Attributes:
        calorie_unit_id (int): The unique identifier for the calorie unit.
        name (str): The name of the calorie unit.
        abbreviation (str): The abbreviation of the calorie unit.
    """
    calorie_unit_id: int
    name: str
    abbreviation: str
    
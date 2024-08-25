from pydantic import BaseModel


class CalorieUnit(BaseModel):
    calorie_unit_id: int
    name: str
    abbreviation: str
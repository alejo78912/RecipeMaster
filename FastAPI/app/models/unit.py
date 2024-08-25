from pydantic import BaseModel


class Unit(BaseModel):
    unit_id: int
    name: str
    abbreviation: str
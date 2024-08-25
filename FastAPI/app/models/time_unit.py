from pydantic import BaseModel


class TimeUnit(BaseModel):
    time_unit_id: int
    name: str
    abbreviation: str
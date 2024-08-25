from pydantic import BaseModel

class Pantry(BaseModel):
    pantry_id: int
    group_id: int
    
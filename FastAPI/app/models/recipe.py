from pydantic import BaseModel


class Recipe(BaseModel):
    recipe_id: int
    title: str
    description: str
    instructions: str
    cooking_time: int
    difficulty: str
    is_public: bool
    total_calories: float
    group_id: int
    time_unit_id: int
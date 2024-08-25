from pydantic import BaseModel


class RecipeCategory(BaseModel):
    category_id: int
    name: str
    description: str
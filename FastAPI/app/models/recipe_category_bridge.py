from pydantic import BaseModel


class RecipeCategoryBridge(BaseModel):
    recipe_id: int
    category_id: int
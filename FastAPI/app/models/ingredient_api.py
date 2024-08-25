from pydantic import BaseModel


class IngredientAPI(BaseModel):
    ingredient_id: int 
    api_id: str
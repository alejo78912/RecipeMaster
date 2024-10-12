from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, DateTime, Text, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Shared metadata object
metadata = MetaData()

# Use the shared metadata
Base = declarative_base(metadata=metadata)

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    phone_number = Column(String(20), nullable=True)
    profile_picture = Column(String(255), nullable=True)
    creation_date = Column(Date)
    update_date = Column(Date)

class Unit(Base):
    __tablename__ = "Unit"
    unit_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    abbreviation = Column(String(10), nullable=False)


class TimeUnit(Base):
    __tablename__ = "TimeUnit"
    time_unit_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    abbreviation = Column(String(10), nullable=False)


class State(Base):
    __tablename__ = "State"
    state_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)


class ShoppingList(Base):
    __tablename__ = "ShoppingList"
    list_id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, nullable=False)
    created_date = Column(Date, nullable=False)
    is_purchased = Column(Boolean, nullable=False)


class ShoppingListItem(Base):
    __tablename__ = "ShoppingListItem"
    list_id = Column(Integer, ForeignKey("ShoppingList.list_id"), primary_key=True)
    ingredient_id = Column(Integer, nullable=False)
    quantity = Column(Float, nullable=False)
    unit_id = Column(Integer, ForeignKey("Unit.unit_id"), nullable=False)


class RecipeIngredient(Base):
    __tablename__ = "RecipeIngredient"
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("Ingredient.ingredient_id"), primary_key=True)
    quantity = Column(Float, nullable=False)
    unit_id = Column(Integer, ForeignKey("Unit.unit_id"), nullable=False)


class Recipe(Base):
    __tablename__ = "Recipe"
    recipe_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    instructions = Column(Text, nullable=True)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(50), nullable=False)
    is_public = Column(Boolean, nullable=False)
    total_calories = Column(Float, nullable=False)
    group_id = Column(Integer, ForeignKey("Group.group_id"), nullable=True)
    time_unit_id = Column(Integer, ForeignKey("TimeUnit.time_unit_id"), nullable=True)


class RecipeCategory(Base):
    __tablename__ = "RecipeCategory"
    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)


class RecipeCategoryBridge(Base):
    __tablename__ = "RecipeCategoryBridge"
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("RecipeCategory.category_id"), primary_key=True)


class Pantry(Base):
    __tablename__ = "Pantry"
    pantry_id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("Group.group_id"), nullable=False)


class PantryItem(Base):
    __tablename__ = "PantryItem"
    pantry_id = Column(Integer, ForeignKey("Pantry.pantry_id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("Ingredient.ingredient_id"), primary_key=True)
    quantity = Column(Float, nullable=False)
    unit_id = Column(Integer, ForeignKey("Unit.unit_id"), nullable=False)
    expiry_date = Column(Date, nullable=True)


class Notification(Base):
    __tablename__ = "Notification"
    notification_id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("Group.group_id"), nullable=False)
    message = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)


class Menu(Base):
    __tablename__ = "Menu"
    menu_id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("Group.group_id"), nullable=False)
    name = Column(String(255), nullable=False)
    total_calories = Column(Float, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)


class MenuRecipe(Base):
    __tablename__ = "MenuRecipe"
    menu_id = Column(Integer, ForeignKey("Menu.menu_id"), primary_key=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), primary_key=True)
    date = Column(DateTime, nullable=True)


class Ingredient(Base):
    __tablename__ = "Ingredient"
    ingredient_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey("Category.category_id"), nullable=True)
    state_id = Column(Integer, ForeignKey("State.state_id"), nullable=True)
    calorie_unit_id = Column(Integer, ForeignKey("CalorieUnit.calorie_unit_id"), nullable=True)
    calories_per_unit = Column(Float, nullable=True)


class Category(Base):
    __tablename__ = "Category"
    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)


class IngredientAPI(Base):
    __tablename__ = "IngredientAPI"
    ingredient_id = Column(Integer, ForeignKey("Ingredient.ingredient_id"), primary_key=True)
    api_id = Column(String(255), primary_key=True)


class Group(Base):
    __tablename__ = "Group"
    group_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)


class GroupMenu(Base):
    __tablename__ = "GroupMenu"
    group_id = Column(Integer, ForeignKey("Group.group_id"), primary_key=True)
    menu_id = Column(Integer, ForeignKey("Menu.menu_id"), primary_key=True)


class GroupMember(Base):
    __tablename__ = "GroupMember"
    group_id = Column(Integer, ForeignKey("Group.group_id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), primary_key=True)
    role = Column(String(50), nullable=False)


class CalorieUnit(Base):
    __tablename__ = "CalorieUnit"
    calorie_unit_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    abbreviation = Column(String(10), nullable=False)
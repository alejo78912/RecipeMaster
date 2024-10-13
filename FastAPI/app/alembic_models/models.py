"""
SQLAlchemy models for the ReceiptMaster application.

This module defines the database schema using SQLAlchemy ORM. It includes models
for users, groups, recipes, ingredients, shopping lists, and more.
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey, DateTime, Text, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Shared metadata object
metadata = MetaData()

# Use the shared metadata
Base = declarative_base(metadata=metadata)


class UserModel(Base):
    """User model representing the user entity in the database."""
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=False)
    profile_picture = Column(String(255), nullable=True)
    creation_date = Column(String(255), nullable=False)
    update_date = Column(String(255), nullable=False)


class Unit(Base):
    """SQLAlchemy model representing a unit of measurement."""
    __tablename__ = "Unit"
    unit_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    abbreviation = Column(String(10), nullable=False)


class TimeUnit(Base):
    """SQLAlchemy model representing a time unit."""
    __tablename__ = "TimeUnit"
    time_unit_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    abbreviation = Column(String(10), nullable=False)


class State(Base):
    """SQLAlchemy model representing the state of an ingredient."""
    __tablename__ = "State"
    state_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)


class ShoppingList(Base):
    """SQLAlchemy model representing a shopping list."""
    __tablename__ = "ShoppingList"
    list_id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, nullable=False)
    created_date = Column(Date, nullable=False)
    is_purchased = Column(Boolean, nullable=False)


class ShoppingListItem(Base):
    """SQLAlchemy model representing an item in a shopping list."""
    __tablename__ = "ShoppingListItem"
    list_id = Column(Integer, ForeignKey("ShoppingList.list_id"), primary_key=True)
    ingredient_id = Column(Integer, nullable=False)
    quantity = Column(Float, nullable=False)
    unit_id = Column(Integer, ForeignKey("Unit.unit_id"), nullable=False)


class RecipeIngredient(Base):
    """SQLAlchemy model representing the relationship between a recipe and its ingredients."""
    __tablename__ = "RecipeIngredient"
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("Ingredient.ingredient_id"), primary_key=True)
    quantity = Column(Float, nullable=False)
    unit_id = Column(Integer, ForeignKey("Unit.unit_id"), nullable=False)


class Recipe(Base):
    """SQLAlchemy model representing a recipe."""
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
    """SQLAlchemy model representing a category for recipes."""
    __tablename__ = "RecipeCategory"
    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)


class RecipeCategoryBridge(Base):
    """SQLAlchemy model representing the relationship between recipes and categories."""
    __tablename__ = "RecipeCategoryBridge"
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("RecipeCategory.category_id"), primary_key=True)


class Pantry(Base):
    """SQLAlchemy model representing a pantry for a group."""
    __tablename__ = "Pantry"
    pantry_id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("Group.group_id"), nullable=False)


class PantryItem(Base):
    """SQLAlchemy model representing an item in a pantry."""
    __tablename__ = "PantryItem"
    pantry_id = Column(Integer, ForeignKey("Pantry.pantry_id"), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey("Ingredient.ingredient_id"), primary_key=True)
    quantity = Column(Float, nullable=False)
    unit_id = Column(Integer, ForeignKey("Unit.unit_id"), nullable=False)
    expiry_date = Column(Date, nullable=True)


class Notification(Base):
    """SQLAlchemy model representing a notification for a group."""
    __tablename__ = "Notification"
    notification_id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("Group.group_id"), nullable=False)
    message = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)


class Menu(Base):
    """SQLAlchemy model representing a menu for a group."""
    __tablename__ = "Menu"
    menu_id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("Group.group_id"), nullable=False)
    name = Column(String(255), nullable=False)
    total_calories = Column(Float, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)


class MenuRecipe(Base):
    """SQLAlchemy model representing the relationship between menus and recipes."""
    __tablename__ = "MenuRecipe"
    menu_id = Column(Integer, ForeignKey("Menu.menu_id"), primary_key=True)
    recipe_id = Column(Integer, ForeignKey("Recipe.recipe_id"), primary_key=True)
    date = Column(DateTime, nullable=True)


class Ingredient(Base):
    """SQLAlchemy model representing an ingredient."""
    __tablename__ = "Ingredient"
    ingredient_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey("Category.category_id"), nullable=True)
    state_id = Column(Integer, ForeignKey("State.state_id"), nullable=True)
    calorie_unit_id = Column(Integer, ForeignKey("CalorieUnit.calorie_unit_id"), nullable=True)
    calories_per_unit = Column(Float, nullable=True)


class Category(Base):
    """SQLAlchemy model representing a category."""
    __tablename__ = "Category"
    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)


class IngredientAPI(Base):
    """SQLAlchemy model representing the relationship between ingredients and external APIs."""
    __tablename__ = "IngredientAPI"
    ingredient_id = Column(Integer, ForeignKey("Ingredient.ingredient_id"), primary_key=True)
    api_id = Column(String(255), primary_key=True)


class Group(Base):
    """SQLAlchemy model representing a group."""
    __tablename__ = "Group"
    group_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)


class GroupMenu(Base):
    """SQLAlchemy model representing the relationship between a group and its menus."""
    __tablename__ = "GroupMenu"
    group_id = Column(Integer, ForeignKey("Group.group_id"), primary_key=True)
    menu_id = Column(Integer, ForeignKey("Menu.menu_id"), primary_key=True)


class GroupMember(Base):
    """SQLAlchemy model representing the relationship between groups and users."""
    __tablename__ = "GroupMember"
    group_id = Column(Integer, ForeignKey("Group.group_id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), primary_key=True)
    role = Column(String(50), nullable=False)


class CalorieUnit(Base):
    """SQLAlchemy model representing a unit for measuring calories."""
    __tablename__ = "CalorieUnit"
    calorie_unit_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    abbreviation = Column(String(10), nullable=False)
    
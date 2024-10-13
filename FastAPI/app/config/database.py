"""
Database models for the ReceiptMaster application.

This module defines the database models using Peewee ORM to interact with a MySQL database.
"""

import os
from dotenv import load_dotenv
from peewee import (
    MySQLDatabase,
    Model,
    AutoField,
    CharField,
    ForeignKeyField,
    IntegerField,
    DecimalField,
    DateField,
    TextField,
    BooleanField,
    DateTimeField,
    CompositeKey
)

# Load environment variables
load_dotenv()

# Set up the database connection
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class UserModel(Model):
    """User model representing the user entity in the database."""
    id = AutoField(primary_key=True)
    username = CharField(max_length=255, null=False)
    email = CharField(max_length=255, null=False)
    password = CharField(max_length=255, null=False)
    phone_number = CharField(max_length=20, null=False)
    profile_picture = CharField(max_length=255, null=True)
    creation_date = CharField(max_length=255, null=False)
    update_date = CharField(max_length=255, null=False)

    class Meta:
        database = database
        table_name = "User"


class GroupModel(Model):
    """Group model representing a group entity."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    description = TextField(null=True)
    creation_date = DateField()
    update_date = DateField()

    class Meta:
        database = database
        table_name = "Group"


class GroupMemberModel(Model):
    """GroupMember model for associating users with groups and roles."""
    group = ForeignKeyField(GroupModel, backref='members')
    user = ForeignKeyField(UserModel, backref='groups')
    role = CharField(max_length=50)
    creation_date = DateField()
    update_date = DateField()

    class Meta:
        database = database
        table_name = "GroupMember"
        primary_key = CompositeKey('group', 'user')


class GroupMenuModel(Model):
    """GroupMenu model representing the menus for groups."""
    group = ForeignKeyField(GroupModel, backref='menus')
    menu_id = IntegerField()
    creation_date = DateField()
    update_date = DateField()

    class Meta:
        database = database
        table_name = "GroupMenu"
        primary_key = CompositeKey('group', 'menu_id')


class RecipeModel(Model):
    """Recipe model representing a recipe."""
    id = AutoField(primary_key=True)
    title = CharField(max_length=255)
    description = TextField(null=True)
    instructions = TextField(null=True)
    cooking_time = IntegerField(null=True)
    difficulty = CharField(max_length=50, null=True)
    is_public = BooleanField()
    total_calories = DecimalField(max_digits=10, decimal_places=2, null=True)
    creation_date = DateField()
    update_date = DateField()
    group = ForeignKeyField(GroupModel, backref='recipes', null=True)

    class Meta:
        database = database
        table_name = "Recipe"


class RecipeCategoryModel(Model):
    """RecipeCategory model representing recipe categories."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    description = TextField(null=True)

    class Meta:
        database = database
        table_name = "RecipeCategory"


class RecipeCategoryBridgeModel(Model):
    """Model representing a many-to-many relationship between recipes and categories."""
    recipe = ForeignKeyField(RecipeModel, backref='categories')
    category = ForeignKeyField(RecipeCategoryModel, backref='recipes')

    class Meta:
        database = database
        table_name = "RecipeCategoryBridge"
        primary_key = CompositeKey('recipe', 'category')


class IngredientModel(Model):
    """Ingredient model representing ingredients in the system."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    category = ForeignKeyField('self', backref='ingredients', null=True)  # Use Category model if defined
    state = ForeignKeyField('self', backref='states', null=True)  # Use State model if defined
    calorie_unit = ForeignKeyField('self', backref='units', null=True)  # Use CalorieUnit model if defined
    calories_per_unit = DecimalField(max_digits=10, decimal_places=2, null=True)
    creation_date = DateField()
    update_date = DateField()

    class Meta:
        database = database
        table_name = "Ingredient"


class IngredientAPIModel(Model):
    """IngredientAPI model linking ingredients to external APIs."""
    ingredient = ForeignKeyField(IngredientModel, backref='apis')
    api_id = CharField(max_length=255)

    class Meta:
        database = database
        table_name = "IngredientAPI"
        primary_key = CompositeKey('ingredient', 'api_id')


class CalorieUnitModel(Model):
    """CalorieUnit model representing calorie measurement units."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    abbreviation = CharField(max_length=10)

    class Meta:
        database = database
        table_name = "CalorieUnit"


class CategoryModel(Model):
    """Category model representing categories."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    description = TextField(null=True)

    class Meta:
        database = database
        table_name = "Category"


class StateModel(Model):
    """State model representing the state of ingredients."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    description = TextField(null=True)

    class Meta:
        database = database
        table_name = "State"


class UnitModel(Model):
    """Unit model representing measurement units."""
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    abbreviation = CharField(max_length=10)

    class Meta:
        database = database
        table_name = "Unit"


class RecipeIngredientModel(Model):
    """RecipeIngredient model linking ingredients to recipes."""
    recipe = ForeignKeyField(RecipeModel, backref='ingredients')
    ingredient = ForeignKeyField(IngredientModel, backref='recipes')
    quantity = DecimalField(max_digits=10, decimal_places=2)
    unit = ForeignKeyField(UnitModel, backref='recipe_ingredients', null=True)
    creation_date = DateField()
    update_date = DateField()

    class Meta:
        database = database
        table_name = "RecipeIngredient"
        primary_key = CompositeKey('recipe', 'ingredient')


class MenuModel(Model):
    """Menu model representing group menus."""
    id = AutoField(primary_key=True)
    group = ForeignKeyField(GroupModel, backref='menus', null=True)
    name = CharField(max_length=255)
    total_calories = DecimalField(max_digits=10, decimal_places=2, null=True)
    start_date = DateField(null=True)
    end_date = DateField(null=True)
    creation_date = DateField()
    update_date = DateField()

    class Meta:
        database = database
        table_name = "Menu"


class MenuRecipeModel(Model):
    """MenuRecipe model linking recipes to menus."""
    menu = ForeignKeyField(MenuModel, backref='recipes')
    recipe = ForeignKeyField(RecipeModel, backref='menus')
    date = DateTimeField(null=True)
    creation_date = DateTimeField()
    update_date = DateTimeField()

    class Meta:
        database = database
        table_name = "MenuRecipe"
        primary_key = CompositeKey('menu', 'recipe')


class ShoppingListModel(Model):
    """ShoppingList model representing shopping lists."""
    id = AutoField(primary_key=True)
    group = ForeignKeyField(GroupModel, backref='shopping_lists', null=True)
    created_date = DateField()
    is_purchased = BooleanField()
    creation_date = DateField()
    update_date = DateField()

    class Meta:
        database = database
        table_name = "ShoppingList"


class ShoppingListItemModel(Model):
    """ShoppingListItem model linking ingredients to shopping lists."""
    list = ForeignKeyField(ShoppingListModel, backref='items')
    ingredient = ForeignKeyField(IngredientModel, backref='shopping_list_items')
    quantity = DecimalField(max_digits=10, decimal_places=2)
    unit = ForeignKeyField(UnitModel, backref='shopping_list_items', null=True)
    creation_date = DateField()
    update_date = DateField()

    class Meta:
        database = database
        table_name = "ShoppingListItem"
        primary_key = CompositeKey('list', 'ingredient')


class PantryModel(Model):
    """Pantry model representing pantries for groups."""
    id = AutoField(primary_key=True)
    group = ForeignKeyField(GroupModel, backref='pantries')
    creation_date = DateField()
    update_date = DateField()

    class Meta:
        database = database
        table_name = "Pantry"


class PantryItemModel(Model):
    """PantryItem model linking ingredients to pantries."""
    pantry = ForeignKeyField(PantryModel, backref='items')
    ingredient = ForeignKeyField(IngredientModel, backref='pantry_items')
    quantity = DecimalField(max_digits=10, decimal_places=2)
    unit = ForeignKeyField(UnitModel, backref='pantry_items', null=True)
    expiry_date = DateField(null=True)
    creation_date = DateField()
    update_date = DateField()

    class Meta:
        database = database
        table_name = "PantryItem"
        primary_key = CompositeKey('pantry', 'ingredient')


class NotificationModel(Model):
    """Notification model representing notifications for groups."""
    id = AutoField(primary_key=True)
    group = ForeignKeyField(GroupModel, backref='notifications', null=True)
    message = TextField()
    date = DateField()
    creation_date = DateField()
    update_date = DateField()

    class Meta:
        database = database
        table_name = "Notification"


class TimeUnitModel(Model):
    """TimeUnit model representing time units."""
    time_unit_id = AutoField(primary_key=True)
    name = CharField()
    abbreviation = CharField()

    class Meta:
        database = database
        table_name = "TimeUnit"
        
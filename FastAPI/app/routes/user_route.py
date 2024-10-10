"""
user_route.py
This module defines the routes for user management in the FastAPI application.
"""

from fastapi import APIRouter, Body, HTTPException, status
from models.user import User  # This should be the Pydantic model representing your input/output data
from services.user_service import UserService
from peewee import DoesNotExist

user_router = APIRouter()


@user_router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user: User = Body(...)):
    """
    Create a new user.

    Args:
        user (User): The user details from the request body.

    Returns:
        User: The newly created user.

    Raises:
        HTTPException: If a user with the same details already exists (400).
    """
    try:
        created_user = UserService.create_user(user)
        return created_user
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@user_router.get("/users", response_model=list[User])
async def get_all_users():
    """
    Retrieve all users.

    Returns:
        list[User]: A list of all registered users.
    """
    users = UserService.get_all_users()
    return users


@user_router.get("/user/{id_user}", response_model=User)
async def get_user_by_id(id_user: int):
    """
    Retrieve a user by their ID.

    Args:
        id_user (int): The unique ID of the user.

    Returns:
        User: The user object with the specified ID.

    Raises:
        HTTPException: If the user is not found (404).
    """
    try:
        return UserService.get_user_by_id(id_user)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@user_router.delete("/user/{id_user}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id_user: int):
    """
    Delete a user by their ID.

    Args:
        id_user (int): The unique ID of the user to delete.

    Raises:
        HTTPException: If the user does not exist (404).
    """
    try:
        UserService.delete_user(id_user)
        return None
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@user_router.put("/user/{id_user}", response_model=User)
async def update_user(id_user: int, user: User = Body(...)):
    """
    Update the details of an existing user.

    Args:
        id_user (int): The unique ID of the user to update.
        user (User): The updated user data.

    Returns:
        User: The updated user object.

    Raises:
        HTTPException: If the user is not found (404).
    """
    try:
        user.id_user = id_user
        updated_user = UserService.update_user(user)
        return updated_user
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
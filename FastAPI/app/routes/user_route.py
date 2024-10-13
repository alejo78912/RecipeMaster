"""
user_route.py
This module defines the routes for user management in the FastAPI application.
"""

from fastapi import APIRouter, Body, HTTPException, status
from models.user import User  # This should be the Pydantic model representing your input/output data
from services.user_service import UserService

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
        return UserService.create_user(user)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    
@user_router.get("/users", response_model=list[User])
async def get_all_users():
    """
    Retrieve all users and return them as Pydantic models.

    Returns:
        list[User]: A list of all registered users.
    """
    return UserService.get_all_users()


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
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@user_router.delete("/user/{id_user}", status_code=status.HTTP_200_OK)
async def delete_user(id_user: int):
    """
    Delete a user by their ID.

    Args:
        id_user (int): The unique ID of the user to delete.

    Raises:
        HTTPException: If the user does not exist (404).
    """
    try:
        # Try to delete the user
        UserService.delete_user(id_user)
        return {"message": f"User with ID {id_user} was successfully deleted."}
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=f"User with ID {id_user} not found.") from exc

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
        return UserService.update_user(id_user, user)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    
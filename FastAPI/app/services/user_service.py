"""
Module for user service class and methods for user management.
"""

from peewee import DoesNotExist
from config.database import UserModel


class UserService:
    """
    Service class for handling user-related operations.

    Methods:
        create_user(user_data: UserModel): Create a new user in the database.
        get_user_by_id(id_user: int): Get a user by its ID.
        get_all_users(): Get all users from the database.
        update_user(user_data: UserModel): Update a user in the database.
        delete_user(id_user: int): Delete a user from the database.

    Raises:
        ValueError: If the user already exists.
        DoesNotExist: If the user does not exist.
    """

    @staticmethod
    def create_user(user_data: UserModel) -> UserModel:
        """
        Create a new user in the database.

        Args:
            user_data (UserModel): The user object to be created.

        Returns:
            UserModel: The created user object.

        Raises:
            ValueError: If the user already exists.
        """
        # Check if the user already exists
        if UserModel.select().where(UserModel.username == user_data.username).exists():
            raise ValueError("User already exists")

        # Create a new user record
        new_user = UserModel(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password,
            phone_number=user_data.phone_number,
            profile_picture=user_data.profile_picture,  # Nullable field
            creation_date=user_data.creation_date,
            update_date=user_data.update_date
        )
        new_user.save()
        return new_user

    @staticmethod
    def get_user_by_id(id_user: int) -> UserModel:
        """
        Get a user by their ID.

        Args:
            id_user (int): The ID of the user.

        Returns:
            UserModel: The user object.

        Raises:
            DoesNotExist: If the user does not exist.
        """
        try:
            return UserModel.get(UserModel.id == id_user)
        except DoesNotExist as exc:
            raise ValueError("User does not exist") from exc

    @staticmethod
    def get_all_users() -> list[UserModel]:
        """
        Get all users from the database.

        Returns:
            list[UserModel]: A list of user objects.
        """
        users = list(UserModel.select())
        return users
    
    @staticmethod
    def update_user(id_user: int, user_data: UserModel) -> UserModel:
        """
        Update a user in the database.

        Args:
            id_user (int): The ID of the user to be updated.
            user_data (UserModel): The updated user data.

        Returns:
            UserModel: The updated user object.

        Raises:
            DoesNotExist: If the user does not exist.
        """
        try:
            # Fetch the existing user
            existing_user = UserModel.get(UserModel.id == id_user)

            # Update user details
            existing_user.username = user_data.username
            existing_user.email = user_data.email
            existing_user.phone_number = user_data.phone_number
            existing_user.password = user_data.password
            existing_user.profile_picture = user_data.profile_picture  # Nullable field

            # Save updated user to the database
            existing_user.save()
            return existing_user
        except DoesNotExist as exc:
            raise ValueError("User does not exist") from exc

    @staticmethod
    def delete_user(id_user: int) -> None:
        """
        Delete a user from the database.

        Args:
            id_user (int): The ID of the user to be deleted.

        Raises:
            DoesNotExist: If the user does not exist.
        """
        try:
            # Fetch the user to be deleted
            user = UserModel.get(UserModel.id == id_user)
            # Delete the user instance from the database
            user.delete_instance()
        except DoesNotExist as exc:
            raise ValueError("User does not exist") from exc
        
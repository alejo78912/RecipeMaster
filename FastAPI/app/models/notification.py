"""
Pydantic models for the Notification entity.
"""

from datetime import datetime  # Correct import for datetime field
from pydantic import BaseModel


class Notification(BaseModel):
    """
    Pydantic model representing a notification for a group.

    Attributes:
        notification_id (int): The unique identifier for the notification.
        group_id (int): The ID of the group the notification is associated with.
        message (str): The content of the notification message.
        date (datetime): The date and time when the notification was created.
    """
    notification_id: int
    group_id: int
    message: str
    date: datetime  # Specify `datetime` for a timestamp
    
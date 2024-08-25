import datetime
from pydantic import BaseModel

class Notification(BaseModel):
    notification_id: int
    group_id: int
    message: str
    date: datetime
from pydantic import BaseModel, Field
from datetime import datetime


class PostOut(BaseModel):
    id: int
    title: str
    content: str
    published_at: datetime | None = None

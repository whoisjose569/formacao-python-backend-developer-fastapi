from pydantic import BaseModel, AwareDatetime
from datetime import datetime
from typing import Optional


class PostIn(BaseModel):
    title: str
    content: str
    published_at: AwareDatetime | None = None
    published: bool = False


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published_at: AwareDatetime | None = None
    published: Optional[bool] = None

from pydantic import BaseModel, AwareDatetime, NaiveDatetime
from typing import Optional


class PostIn(BaseModel):
    title: str
    content: str
    published_at: AwareDatetime | NaiveDatetime | None
    published: bool = False


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published_at: AwareDatetime | NaiveDatetime | None
    published: Optional[bool] = None

from pydantic import BaseModel
from typing import Text, Optional
from datetime import date, datetime
from uuid import uuid4 as uuid

class Post(BaseModel):
    id: Optional[str] = uuid()
    title: str 
    author: str 
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False
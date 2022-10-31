from typing import Optional
from pydantic import BaseModel

class TodoItem(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    class Config:
        orm_mode = True
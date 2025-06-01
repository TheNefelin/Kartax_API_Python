from pydantic import BaseModel
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str
    img: str


class CategoryOut(CategoryCreate):
    id: int
    is_enable: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Esto reemplaza a 'orm_mode = True' en Pydantic v2
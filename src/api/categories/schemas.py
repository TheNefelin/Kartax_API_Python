from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CategoryId(BaseModel):
    id: int

class CategoryBase(BaseModel):
    name: str
    img: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryPatch(BaseModel):
    name: Optional[str] = None
    img: Optional[str] = None

class CategoryOut(CategoryBase, CategoryId):
    is_enable: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Necesario para leer desde SQLAlchemy

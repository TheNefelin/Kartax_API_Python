from datetime import datetime
from pydantic import BaseModel, ConfigDict

class GroupId(BaseModel):
    id: int

class GroupBase(BaseModel):
    category_id: int
    name: str

class GroupCreate(GroupBase):
    pass

class GroupUpdate(GroupBase, GroupId):
    pass

class GroupOut(GroupBase, GroupId):
    is_enable: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
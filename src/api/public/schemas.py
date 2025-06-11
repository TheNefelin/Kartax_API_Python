from typing import List, Optional

from pydantic import BaseModel, ConfigDict

class ProductPublicOut(BaseModel):
    id: int
    group_id: int
    parent_product_id: Optional[int]
    name: str
    description: str
    img: str
    is_fractional: bool
    base_unit: str
    sale_unit: Optional[float]
    stock: float
    waste_percentage: Optional[float]
    is_enable: bool

    model_config = ConfigDict(from_attributes=True)

class GroupPublicOut(BaseModel):
    id: int
    category_id: int
    name: str
    is_enable: bool
    products: List[ProductPublicOut]

    model_config = ConfigDict(from_attributes=True)

class CategoryPublicOut(BaseModel):
    id: int
    name: str
    img: str
    is_enable: bool
    groups: List[GroupPublicOut]

    model_config = ConfigDict(from_attributes=True)
    
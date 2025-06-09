from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class ProductId(BaseModel):
    id: int
    group_id: int

class ProductBase(BaseModel):
    parent_product_id: int
    name: str
    description: str
    img: str
    is_fractional: bool
    base_unit: str
    sale_unit: float
    stock: int
    waste_percentage: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase, ProductId):
    pass

# class ProductPatch(BaseModel, ProductId):
#     parent_product_id: int
#     name: Optional[str]
#     description: Optional[str]
#     img: Optional[str]
#     is_fractional: Optional[bool]
#     base_unit: Optional[str]
#     sale_unit: Optional[float]
#     stock: Optional[int]
#     waste_percentage: Optional[int]
    
class ProductOut(BaseModel):
    id: int
    group_id: int
    parent_product_id: Optional[int]
    name: str
    description: str
    img: str
    is_fractional: bool
    base_unit: str
    sale_unit: Optional[float]
    stock: int
    waste_percentage: Optional[int]
    is_enable: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
from sqlalchemy import Column, Integer, String, Boolean, Numeric, DateTime, ForeignKey, func, text
from sqlalchemy.orm import relationship

from src.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    parent_product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    name = Column(String(100), nullable=False)
    description = Column(String(256), nullable=False)
    price = Column(Integer, nullable=False, default=0)
    img = Column(String(100), nullable=False)
    is_fractional = Column(Boolean, default=False, server_default=text('false'), nullable=False)
    base_unit = Column(String(20), nullable=False)
    sale_unit = Column(Numeric, nullable=True)
    stock = Column(Numeric, default=0)
    waste_percentage = Column(Numeric(5, 2), default=0)
    is_enable = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relaciones
    group = relationship("Group", backref="products")
    parent_product = relationship("Product", remote_side=[id], backref="child_products")

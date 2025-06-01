from src.core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime, Text, CheckConstraint, func
from sqlalchemy.orm import relationship

class StockMovement(Base):
    __tablename__ = "stock_movements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    movement_type = Column(String(20), nullable=False)
    quantity = Column(Numeric, nullable=False)
    movement_date = Column(DateTime, server_default=func.now())
    note = Column(Text)

    # Restricción CHECK
    __table_args__ = (
        CheckConstraint(
            "movement_type IN ('sale', 'adjustment', 'restock')",
            name="check_movement_type"
        ),
    )

    # Relaciones
    product = relationship("Product", backref="stock_movements")

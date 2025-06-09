from sqlalchemy.orm import Session

from src.api.products import models
from src.shared.responses import ResponseModel

def get_products(db: Session):
    db_products = db.query(models.Product).all()
    return ResponseModel.Success(data=db_products)
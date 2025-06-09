from typing import List
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from src.api.products import crud, schemas
from src.core.database import get_db
from src.shared.responses import ResponseModel

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=ResponseModel[List[schemas.ProductOut]])
def get_products(response: Response, db: Session = Depends(get_db)):
    res = crud.get_products(db)
    response.status_code = res.statusCode
    return res

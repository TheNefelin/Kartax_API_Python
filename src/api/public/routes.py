from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from src.api.public import crud, schemas
from src.core.database import get_db
from src.shared.responses import ResponseModel

router = APIRouter(prefix="/public", tags=["public"])

@router.get("/products", response_model=ResponseModel[list[schemas.CategoryPublicOut]])
def get_public_products(response: Response, db: Session = Depends(get_db)):
    res = crud.get_categories_with_groups_and_products(db)
    response.status_code = res.statusCode
    return res
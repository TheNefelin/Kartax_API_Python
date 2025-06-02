from fastapi import APIRouter, Response, Depends
from sqlalchemy.orm import Session
from typing import List

from src.core.database import get_db
from src.shared.responses import ResponseModel
from . import crud, schemas

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=ResponseModel[List[schemas.CategoryOut]])
def get_categories(response: Response, db: Session = Depends(get_db)):
    res = crud.get_categories(db)
    response.status_code = res.statusCode
    return res

@router.get("/{id}", response_model=ResponseModel[schemas.CategoryOut])
def get_category(id: int, response: Response, db: Session = Depends(get_db)):
    res = crud.get_category(db, id)
    response.status_code = res.statusCode
    return res

@router.post("/", response_model=ResponseModel[schemas.CategoryOut])
def create_category(category: schemas.CategoryCreate, response: Response, db: Session = Depends(get_db)):
    res = crud.create_category(db, category)
    response.status_code = res.statusCode
    return res

@router.put("/{id}", response_model=ResponseModel[schemas.CategoryOut])
def update_category(id: int, category: schemas.CategoryCreate, response: Response, db: Session = Depends(get_db)):
    res = crud.update_category(db, id, category)
    response.status_code = res.statusCode
    return res

@router.patch("/{id}", response_model=ResponseModel[schemas.CategoryOut])
def patch_category(id: int, category: schemas.CategoryPatch, response: Response, db: Session = Depends(get_db)):
    res = crud.patch_category(db, id, category)
    response.status_code = res.statusCode
    return res

@router.delete("/{id}", response_model=ResponseModel)
def delete_category(id: int, response: Response, db: Session = Depends(get_db)):
    res = crud.delete_category(db, id)
    response.status_code = res.statusCode
    return res

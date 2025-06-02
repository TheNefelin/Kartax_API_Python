from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.shared.responses import ResponseModel
from . import models, schemas

def get_categories(db: Session):
    db_categories = db.query(models.Category).all()
    return ResponseModel.Success(data=db_categories)

def get_category(db: Session, id: int):
    db_category = db.query(models.Category).filter(models.Category.id == id).first()
    if not db_category:
        return ResponseModel.NotFound()
    category_out = schemas.CategoryOut.model_validate(db_category)
    return ResponseModel.Success(data=category_out)

def create_category(db: Session, category: schemas.CategoryCreate):
    try:
        db_category = models.Category(
            name=category.name,
            img=category.img
        )
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        category_out = schemas.CategoryOut.model_validate(db_category)
        return ResponseModel.Created(data=category_out)
    except SQLAlchemyError as e:
        db.rollback()
        return ResponseModel.ServerError(message=str(e))
    
def update_category(db: Session, id: int, category: schemas.CategoryUpdate):
    try:
        db_category = db.query(models.Category).filter(models.Category.id == id).first()
        if not db_category:
            return ResponseModel.NotFound()
        db_category.name = category.name
        db_category.img = category.img
        db.commit()
        db.refresh(db_category)
        category_out = schemas.CategoryOut.model_validate(db_category)
        return ResponseModel.Success(data=category_out)
    except SQLAlchemyError as e:
        db.rollback()
        return ResponseModel.ServerError(message=str(e))

def patch_category(db: Session, id: int, category: schemas.CategoryPatch):
    try:
        db_category = db.query(models.Category).filter(models.Category.id == id).first()
        if not db_category:
            return ResponseModel.NotFound()
        if category.name is None and category.img is None:
            return ResponseModel.BadRequest(message="At least one field (name or img) must be provided.")
        if category.name is not None:
            db_category.name = category.name
        if category.img is not None:
            db_category.img = category.img
        db.commit()
        db.refresh(db_category)
        category_out = schemas.CategoryOut.model_validate(db_category)
        return ResponseModel.Success(data=category_out)
    except SQLAlchemyError as e:
        db.rollback()
        return ResponseModel.ServerError(message=str(e))
    
def delete_category(db: Session, id: int):
    try:
        db_category = db.query(models.Category).filter(models.Category.id == id).first()
        if not db_category:
            return ResponseModel.NotFound()
        db.delete(db_category)
        db.commit()
        return ResponseModel.Success(message="Deleted successfully.")
    except SQLAlchemyError as e:
        db.rollback()
        return ResponseModel.ServerError(message=str(e))

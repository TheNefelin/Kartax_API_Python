from sqlalchemy.orm import Session
from . import models, schemas

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(
        name=category.name,
        img=category.img
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def update_category(db: Session, category_id: int, category_data: schemas.CategoryCreate):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        return None

    category.name = category_data.name
    category.img = category_data.img
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if not category:
        return None

    db.delete(category)
    db.commit()
    return category


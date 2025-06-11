from sqlalchemy.orm import Session, contains_eager
from sqlalchemy.exc import SQLAlchemyError

from src.api.categories.models import Category
from src.api.groups.models import Group
from src.api.products.models import Product
from src.api.public.schemas import CategoryPublicOut
from src.shared.responses import ResponseModel

def get_categories_with_groups_and_products(db: Session):
    try:
        query = db.query(Category).join(Category.groups).join(Group.products).filter(
            Category.is_enable == True,
            Group.is_enable == True,
            Product.is_enable == True,
            Product.is_fractional == False
        ).options(
            contains_eager(Category.groups)
            .contains_eager(Group.products)
        ).distinct()

        categories = query.all()

        from_orm_to_schema = [CategoryPublicOut.model_validate(cat) for cat in categories]
        
        return ResponseModel.Success(data=from_orm_to_schema)
    except SQLAlchemyError as e:
        return ResponseModel.ServerError(message=str(e))

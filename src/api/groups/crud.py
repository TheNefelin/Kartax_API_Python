from sqlalchemy.orm import Session

from src.api.groups import models
from src.shared.responses import ResponseModel

def get_groups(db: Session):
    db_groups = db.query(models.Group).all()
    return ResponseModel.Success(data=db_groups)

from typing import List
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session

from src.api.groups import crud, schemas
from src.core.database import get_db
from src.shared.responses import ResponseModel

router = APIRouter(prefix="/groups", tags=["groups"])

@router.get("/", response_model=ResponseModel[List[schemas.GroupOut]])
def get_groups(response: Response, db: Session = Depends(get_db)):
    res = crud.get_groups(db)
    response.status_code = res.statusCode
    return res
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel
from src.core.config import settings

T = TypeVar("T")

class ResponseModel(BaseModel, Generic[T]):
    isSuccess: bool
    statusCode: int
    status: str
    message: Optional[str]
    data: Optional[T]

    # Get, Update, Patch, Delete
    @classmethod
    def Success(cls, data: Optional[T] = None, message: Optional[str] = None,):
        return cls(
            isSuccess=True,
            statusCode=200,
            status="success",
            message=message,
            data=data,
        )
    
    # Create
    @classmethod
    def Created(cls, data: Optional[T] = None, message: Optional[str] = None):
        return cls(
            isSuccess=True,
            statusCode=201,
            status="Created",
            message=message,
            data=data,
        )
        
    # Delete, Update
    @classmethod
    def NoContent(cls):
        return cls(
            isSuccess=True,
            statusCode=204,
            status="No Content",
            message=None,
            data=None
        )

    @classmethod
    def BadRequest(cls, message: Optional[str] = None):
        return cls(
            isSuccess=False,
            statusCode=400,
            status="Bad Request",
            message=message,
            data=None,
        )

    @classmethod
    def Unauthorized(cls, message: Optional[str] = None):
        return cls(
            isSuccess=False,
            statusCode=401,
            status="Unauthorized",
            message=message,
            data=None
        )
    
    @classmethod
    def NotFound(cls, message: Optional[str] = None):
        return cls(
            isSuccess=False,
            statusCode=404,
            status="Not Found",
            message=message,
            data=None,
        )
        
    @classmethod
    def ServerError(cls, message: Optional[str] = "An unexpected error occurred."):
        return cls(
            isSuccess=False,
            statusCode=500,
            status="Internal Server Error",
            message=message if settings.debug else "An unexpected error occurred.",
            data=None,
        )
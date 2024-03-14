from typing import TypeVar, Generic, Optional, Any
from pydantic import BaseModel, Field

DataT = TypeVar('DataT')

class BaseResponseModel(BaseModel, Generic[DataT]):
    status_code: int = Field(..., description="HTTP status code of the response.")
    message: Optional[str] = Field(None, description="A message about the response.")
    data: Optional[DataT] = Field(None, description="The data payload of the response.")

class SuccessResponseModel(BaseResponseModel[DataT]):
    pass

class ErrorDetail(BaseModel):
    detail: Any = Field(..., description="Detailed information about the error.")
    path: Optional[str] = Field(None, description="The request path where the error occurred, if applicable.")

class ErrorResponseModel(BaseResponseModel[ErrorDetail]):
    pass
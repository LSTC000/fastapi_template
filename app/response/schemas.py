from enum import Enum
from typing import Optional

from pydantic import BaseModel


class StatusType(Enum):
    success: str = 'success'
    error: str = 'error'


class BaseAPIResponse(BaseModel):
    status: StatusType
    data: Optional[dict] = None
    details: Optional[str] = None

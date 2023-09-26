from enum import Enum
from typing import Optional

from .details import Details

from pydantic import BaseModel


class StatusType(Enum):
    success: str = 'success'
    error: str = 'error'


class BaseAPIResponse(BaseModel):
    status: Optional[StatusType] = StatusType.success
    data: Optional[dict] = {}
    detail: Optional[str] = Details.success_status

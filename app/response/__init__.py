__all__ = ['BaseAPIResponse', 'StatusType', 'detail']


from .schemas import BaseAPIResponse, StatusType
from .detail import Detail

detail = Detail()

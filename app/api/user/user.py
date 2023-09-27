from app.common import config, Logger
from app.utils.response import BaseAPIResponse, StatusType

from .schemas import UserSchema, UserAddSchema, UserEditSchema
from .services import UserService, UserEmailService
from .dependencies import user_service, user_email_service
from .details import UserDetails

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError


router = APIRouter(prefix='/user', tags=['User'])

logger = Logger(name=__name__, log_path=config.user_log_path).get_logger()


@router.get('/{user_id}', response_model=BaseAPIResponse)
async def get_user(
        user_id: int,
        service: UserService = Depends(user_service),
        email_service: UserEmailService = Depends(user_email_service)
):
    response = BaseAPIResponse()
    try:
        user_data = await service.get_user(user_id)

        if user_data is not None:
            response.data = {'user_data': UserSchema(**user_data)}
        else:
            response.status = StatusType.error
            response.detail = UserDetails.get_user_error
    except HTTPException as exc:
        response.status = StatusType.error
        response.detail = exc.detail
    except Exception as exc:
        logger.error(exc)
        email_service.send_error_log(str(exc))
        response.status = StatusType.error
        response.detail = UserDetails.exception_error
    finally:
        return response


@router.post('/', response_model=BaseAPIResponse)
async def add_user(
        user_data: UserAddSchema,
        service: UserService = Depends(user_service),
        email_service: UserEmailService = Depends(user_email_service)
):
    response = BaseAPIResponse()
    try:
        user_id = await service.add_user(user_data)

        if user_id is not None:
            response.data = {'user_id': user_id}
        else:
            response.status = StatusType.error
            response.detail = UserDetails.add_user_error
    except IntegrityError:
        response.status = StatusType.error
        response.detail = UserDetails.email_exist
    except HTTPException as exc:
        response.status = StatusType.error
        response.detail = exc.detail
    except Exception as exc:
        logger.error(exc)
        email_service.send_error_log(str(exc))
        response.status = StatusType.error
        response.detail = UserDetails.exception_error
    finally:
        return response


@router.patch('/', response_model=BaseAPIResponse)
async def edit_user(
        user_id: int,
        new_user_data: UserEditSchema,
        service: UserService = Depends(user_service),
        email_service: UserEmailService = Depends(user_email_service)
):
    response = BaseAPIResponse()
    try:
        user_id = await service.edit_user(user_id=user_id, new_user_data=new_user_data)

        if user_id is not None:
            response.data = {'user_id': user_id}
        else:
            response.status = StatusType.error
            response.detail = UserDetails.edit_user_error
    except HTTPException as exc:
        response.status = StatusType.error
        response.detail = exc.detail
    except Exception as exc:
        logger.error(exc)
        email_service.send_error_log(str(exc))
        response.status = StatusType.error
        response.detail = UserDetails.exception_error
    finally:
        return response


@router.delete('/', response_model=BaseAPIResponse)
async def delete_user(
        user_id: int,
        service: UserService = Depends(user_service),
        email_service: UserEmailService = Depends(user_email_service)
):
    response = BaseAPIResponse()
    try:
        user_id = await service.delete_user(user_id)

        if user_id is not None:
            response.data = {'user_id': user_id}
        else:
            response.status = StatusType.error
            response.detail = UserDetails.delete_user_error
    except HTTPException as exc:
        response.status = StatusType.error
        response.detail = exc.detail
    except Exception as exc:
        logger.error(exc)
        email_service.send_error_log(str(exc))
        response.status = StatusType.error
        response.detail = UserDetails.exception_error
    finally:
        return response

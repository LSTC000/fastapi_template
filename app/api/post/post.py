from .schemas import PostSchema, PostAddSchema
from .services import PostDBService, PostEmailService
from .dependencies import post_db_service, post_email_service
from .details import PostDetails

from app.common import config, Logger
from app.utils.response import BaseAPIResponse, StatusType
from app.api.user.schemas import UserSchema

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError


router = APIRouter(prefix='/post', tags=['Post'])

logger = Logger(name=__name__, log_path=config.post_log_path).get_logger()


@router.get('/{post_id}', response_model=BaseAPIResponse)
async def get_post(
        post_id: int,
        db_service: PostDBService = Depends(post_db_service),
        email_service: PostEmailService = Depends(post_email_service)
):
    response = BaseAPIResponse()
    try:
        post_data = await db_service.get_post(post_id)

        if post_data is not None:
            response.data = {'post_data': PostSchema(**post_data)}
        else:
            response.status = StatusType.error
            response.detail = PostDetails.get_post_error
    except HTTPException as exc:
        response.status = StatusType.error
        response.detail = exc.detail
    except Exception as exc:
        response.status = StatusType.error
        response.detail = PostDetails.exception_error
        logger.error(exc)
        email_service.send_error_log(str(exc))
    finally:
        return response


@router.get('/user/{post_id}', response_model=BaseAPIResponse)
async def get_post_user(
        post_id: int,
        db_service: PostDBService = Depends(post_db_service),
        email_service: PostEmailService = Depends(post_email_service)
):
    response = BaseAPIResponse()
    try:
        post_data = await db_service.get_post(post_id, user_data=True)

        if post_data is not None:
            response.data = {
                'user_data': UserSchema(**post_data['user'].__dict__)
            }
        else:
            response.status = StatusType.error
            response.detail = PostDetails.get_post_error
    except HTTPException as exc:
        response.status = StatusType.error
        response.detail = exc.detail
    except Exception as exc:
        response.status = StatusType.error
        response.detail = PostDetails.exception_error
        logger.error(exc)
        email_service.send_error_log(str(exc))
    finally:
        return response


@router.post('/', response_model=BaseAPIResponse)
async def add_post(
        post_data: PostAddSchema,
        db_service: PostDBService = Depends(post_db_service),
        email_service: PostEmailService = Depends(post_email_service)
):
    response = BaseAPIResponse()
    try:
        post_id = await db_service.add_post(post_data)

        if post_id is not None:
            response.data = {'post_id': post_id}
        else:
            response.status = StatusType.error
            response.detail = PostDetails.add_post_error
    except IntegrityError:
        response.status = StatusType.error
        response.detail = PostDetails.user_does_not_exist
    except HTTPException as exc:
        response.status = StatusType.error
        response.detail = exc.detail
    except Exception as exc:
        response.status = StatusType.error
        response.detail = PostDetails.exception_error
        logger.error(exc)
        email_service.send_error_log(str(exc))
    finally:
        return response

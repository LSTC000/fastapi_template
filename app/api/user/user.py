from app.response import BaseAPIResponse, StatusType

from .schemas import UserSchema, UserAddSchema, UserEditSchema
from .services import UserService
from .dependencies import user_service

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix='/user', tags=['User'])


@router.get('/{user_id}', response_model=BaseAPIResponse)
async def get_user(user_id: int, service: UserService = Depends(user_service)):
    try:
        user_data = await service.get_user(user_id)

        return BaseAPIResponse(
            status=StatusType.success.value,
            data={'user_data': UserSchema(**user_data)} if user_data is not None else user_data,
        )
    except HTTPException as exc:
        return BaseAPIResponse(
            status=StatusType.success.error,
            detail=exc.detail
        )


@router.post('/', response_model=BaseAPIResponse)
async def add_user(user_data: UserAddSchema, service: UserService = Depends(user_service)):
    try:
        user_id = await service.add_user(user_data)

        return BaseAPIResponse(
            status=StatusType.success.value,
            data={'user_id': user_id} if user_id is not None else user_id,
        )
    except IntegrityError:
        return BaseAPIResponse(
            status=StatusType.success.error,
            detail='This email already exist'
        )
    except HTTPException as exc:
        return BaseAPIResponse(
            status=StatusType.success.error,
            detail=exc.detail
        )


@router.patch('/', response_model=BaseAPIResponse)
async def edit_user(user_id: int, new_user_data: UserEditSchema, service: UserService = Depends(user_service)):
    try:
        user_id = await service.edit_user(user_id=user_id, new_user_data=new_user_data)

        return BaseAPIResponse(
            status=StatusType.success.value,
            data={'user_id': user_id} if user_id is not None else user_id,
        )
    except HTTPException as exc:
        return BaseAPIResponse(
            status=StatusType.success.error,
            detail=exc.detail
        )


@router.delete('/', response_model=BaseAPIResponse)
async def delete_user(user_id: int, service: UserService = Depends(user_service)):
    try:
        user_id = await service.delete_user(user_id)

        return BaseAPIResponse(
            status=StatusType.success.value,
            data={'user_id': user_id} if user_id is not None else user_id,
        )
    except HTTPException as exc:
        return BaseAPIResponse(
            status=StatusType.success.error,
            detail=exc.detail
        )

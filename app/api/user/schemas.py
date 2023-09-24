from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    id: int
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: EmailStr = Field(max_length=32)
    is_active: bool
    created_at: datetime


class UserAddSchema(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: EmailStr = Field(max_length=32)
    is_active: bool


class UserEditSchema(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)

from pydantic import BaseModel, Field


class PostSchema(BaseModel):
    id: int
    title: str = Field(max_length=100)
    body: str
    user_id: int


class PostAddSchema(BaseModel):
    title: str = Field(max_length=100)
    body: str
    user_id: int

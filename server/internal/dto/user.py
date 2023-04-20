from typing import Any, Callable, Optional
import uuid

from fastapi_users import schemas
from pydantic import EmailStr, Field


class UserRead(schemas.BaseUser[int]):
    id: uuid.UUID
    email: EmailStr
    city: str
    role_id: int

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):

    email: EmailStr
    city: str
    password: str
    role_id: int


class UserUpdate(schemas.BaseUserUpdate):

    email: EmailStr
    city: str
    password: str
    role_id: int

from typing import Optional
from pydantic import BaseModel


class VacancyCreate(BaseModel):
    title: str
    description: str
    gross: Optional[int]


class ApplicationBase(BaseModel):
    pass

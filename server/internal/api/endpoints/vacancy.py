from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException

from internal.crud.vacancy import (
    _create_vacancy,
    _get_all_vacancy,
    _delete_vacancy,
    _get_one_vacancy,
)
from internal.dto.vacancy import VacancyCreate
from internal.db.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/vacancys/")
async def get_all_vacancy(
    vacancy: VacancyCreate, session: AsyncSession = Depends(get_session)
) -> VacancyCreate:
    try:
        return await _get_all_vacancy(vacancy, session)
    except HTTPException as error:
        raise HTTPException(
            status_code=404, detail=f"vacancy not found as {error}")


@router.get("/vacancys/")
async def get_one_vacancy(
    vacancy: VacancyCreate, session: AsyncSession = Depends(get_session)
) -> VacancyCreate:
    try:
        return await _get_one_vacancy(vacancy, session)
    except HTTPException as error:
        raise HTTPException(
            status_code=404, detail=f"vacancy not found as {error}")


@router.post("/vacancys/")
async def create_vacancy(
    vacancy: VacancyCreate, session: AsyncSession = Depends(get_session)
) -> VacancyCreate:
    try:
        return await _create_vacancy(vacancy, session)
    except HTTPException as error:
        raise HTTPException(
            status_code=404, detail=f"vacancy not found as {error}")


@router.delete("/vacancys/")
async def delete_vacancy(
    vacancy: VacancyCreate, session: AsyncSession = Depends(get_session)
) -> VacancyCreate:
    try:
        return await _delete_vacancy(vacancy, session)
    except HTTPException as error:
        raise HTTPException(
            status_code=404, detail=f"vacancy not found as {error}")

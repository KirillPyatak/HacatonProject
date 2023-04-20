from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Request

from internal.crud.application import (
    _create_application,
    _get_all_application,
    _delete_application,
    _get_one_application,
)
from internal.dto.application import ApplicationCreate
from internal.db.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()





@router.get("/applications/")
async def get_all_application(
    application: ApplicationCreate, session: AsyncSession = Depends(get_session)
) -> ApplicationCreate:
    try:
        return await _get_all_application(application, session)
    except HTTPException as error:
        raise HTTPException(
            status_code=404, detail=f"application not found as {error}")


@router.get("/applications/")
async def get_one_application(
    application: ApplicationCreate, session: AsyncSession = Depends(get_session)
) -> ApplicationCreate:
    try:
        return await _get_one_application(application, session)
    except HTTPException as error:
        raise HTTPException(
            status_code=404, detail=f"application not found as {error}")


@router.post("/applications/")
async def create_application(
    application: ApplicationCreate, session: AsyncSession = Depends(get_session)
) -> ApplicationCreate:
    try:
        return await _create_application(application, session)
    except HTTPException as error:
        raise HTTPException(
            status_code=404, detail=f"application not found as {error}")


@router.delete("/applications/")
async def delete_application(
    application: ApplicationCreate, session: AsyncSession = Depends(get_session)
) -> ApplicationCreate:
    try:
        return await _delete_application(application, session)
    except HTTPException as error:
        raise HTTPException(
            status_code=404, detail=f"application not found as {error}")

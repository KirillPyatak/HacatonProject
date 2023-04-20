from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from internal.dto.user import UserRead
from internal.db.models import User
from internal.app.users import current_active_user
from internal.db.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/", description="Endpoint for get user data", response_model=UserRead)
async def get_user_by_uuid(user_id: UUID, db: AsyncSession = Depends(get_session)) -> UserRead:
    """
    Authenticates a user and returns an access token.
    """
    try:
        return await get_user(user_id, db)
    except HTTPException as exception:
        raise HTTPException(
            status_code=503, detail=f"Database error: {exception}")

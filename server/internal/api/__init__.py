from . import endpoints
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(endpoints.router, prefix='/v1')

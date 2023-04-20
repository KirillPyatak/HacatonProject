from internal.app.users import auth_backend, fastapi_users
from internal.dto.user import UserCreate, UserRead, UserUpdate
from fastapi import APIRouter
from . import application,user


router = APIRouter()

router.include_router(
    user.router,
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    application.router,
    prefix="/application",
    tags=["application"],
)
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],

)
router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
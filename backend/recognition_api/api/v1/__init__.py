from fastapi import APIRouter

from .endpoints import root_router

api_v1_router: APIRouter = APIRouter(
    prefix="/api/v1",
)

api_v1_router.include_router(root_router)

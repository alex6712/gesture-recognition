from fastapi import APIRouter

from .model import router as _model_router
from .root import router as _root_router

api_v1_router: APIRouter = APIRouter(
    prefix="/v1",
)

api_v1_router.include_router(_model_router)
api_v1_router.include_router(_root_router)

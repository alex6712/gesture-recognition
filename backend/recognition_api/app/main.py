from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.v1 import api_v1_router
from app.core.config import Settings, get_settings

settings: Settings = get_settings()

tags_metadata = [
    {
        "name": "model",
        "description": "**Gateway** для работы с _моделью компьютерного зрения_.",
    },
    {
        "name": "root",
        "description": "Получение информации о **приложении**.",
    },
]

recognition_api: FastAPI = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    summary=settings.APP_SUMMARY,
    contact={
        "name": settings.ADMIN_NAME,
        "email": settings.ADMIN_EMAIL,
    },
    openapi_tags=tags_metadata,
)

recognition_api.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

recognition_api.include_router(api_v1_router)

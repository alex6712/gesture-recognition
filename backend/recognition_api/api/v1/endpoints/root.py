from typing import Annotated

from fastapi import APIRouter, Depends, status

from core.config import Settings, get_settings
from core.recognition_model_client import get_recognition_model_client, RecognitionModelClient
from schemas.responses import AppInfoResponse, StandardResponse

router = APIRouter(
    tags=["root"],
)


@router.get(
    "/",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    summary="Проверка работоспособности API.",
)
async def root():
    """Корневой путь для проверки работоспособности API.

    Ничего не делает, кроме как возвращает положительный ответ на запрос.

    Returns
    -------
    response : StandardResponse
        Ответ о корректной работе сервера.
    """
    return {"message": "API works!"}


@router.get(
    "/model",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    summary="Проверка работоспособности модели.",
)
async def model():
    """Путь для проверки работоспособности модели.

    Отправляет запрос с использованием gRPC Client. Получает ответ от сервиса модели,
    возвращает ответ модели.

    Returns
    -------
    response : StandardResponse
        Ответ о корректной работе модели.
    """
    recognition_model_client: RecognitionModelClient = get_recognition_model_client()
    return recognition_model_client.healthcheck()


@router.get(
    "/app_info",
    response_model=AppInfoResponse,
    status_code=status.HTTP_200_OK,
    summary="Информация о приложении.",
)
async def app_info(settings: Annotated[Settings, Depends(get_settings)]):
    """Запрос на получение информации о серверной стороне приложения.

    Получаемая информация:
        * app_name: str, имя приложения;
        * app_version: str, версия приложения;
        * app_description: str, полное описание приложения;
        * app_summary: str, краткое описание приложения;
        * admin_name: str, полное имя ответственного лица;
        * admin_email: str, адрес электронной почты для связи с ответственным лицом.

    Parameters
    ----------
    settings : Settings
        Настройки приложения.

    Returns
    -------
    response : AppInfoResponse
        Ответ, содержащий информацию о серверной стороне приложения.
    """
    return {
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
        "app_description": settings.APP_DESCRIPTION,
        "app_summary": settings.APP_SUMMARY,
        "admin_name": settings.ADMIN_NAME,
        "admin_email": settings.ADMIN_EMAIL,
    }

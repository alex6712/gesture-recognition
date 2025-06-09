from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies import get_model_service
from app.schemas.v1.responses import StandardResponse
from app.services import RecognitionModelService

router = APIRouter(
    prefix="/model",
    tags=["model"],
)


@router.get(
    "/",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    summary="Проверка работоспособности модели.",
)
async def model(
    model_service: Annotated[RecognitionModelService, Depends(get_model_service)],
):
    """Путь для проверки работоспособности модели.

    Отправляет запрос с использованием gRPC Client. Получает ответ от сервиса модели,
    возвращает ответ модели.

    Parameters
    ----------
    model_service : RecognitionModelService
        Сервисный слой обслуживания gRPC-сервера модели компьютерного зрения.

    Returns
    -------
    response : StandardResponse
        Ответ о корректной работе модели.
    """
    return await model_service.health_check()

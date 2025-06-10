from typing import TYPE_CHECKING

from fastapi import APIRouter, status

from app.core.dependencies import RecognitionModelServiceDependency
from app.schemas.v1.responses import StandardResponse

if TYPE_CHECKING:
    from app.services.model_service import RecognitionModelService

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
    model_service: RecognitionModelServiceDependency,
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

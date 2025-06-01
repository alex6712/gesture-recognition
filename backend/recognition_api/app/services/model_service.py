from fastapi import status, HTTPException
from grpc import RpcError, StatusCode

from app.repositories import RecognitionModelRepository
from app.schemas.v1.responses import StandardResponse


class RecognitionModelService:
    """Сервисный слой взаимодействия с моделью.

    Представляет собой класс сервисного слоя в реализации паттерна Репозиторий.
    Реализует бизнес-логику при взаимодействии сервиса `RESTful API` и
    моделью компьютерного зрения.

    Attributes
    ----------
    model_repo : RecognitionModelRepository
        Репозиторий модели, слой репозитория.

    Methods
    -------
    health_check()
        Проверка работоспособности модели.
    """
    def __init__(self, model_repo: RecognitionModelRepository):
        self.model_repo: RecognitionModelRepository = model_repo

    async def health_check(self) -> StandardResponse:
        """Проверяет доступность и работоспособность модели машинного обучения.

        Выполняет проверку жизнеспособности модели через RPC-вызов к репозиторию.
        Обрабатывает возможные ошибки взаимодействия с микросервисом модели.

        Returns
        -------
        response : StandardResponse
            Объект стандартизированного ответа от сервера.

        Raises
        ------
        HTTPException
            - 503 SERVICE UNAVAILABLE: Нет соединения с моделью.
            - 500 INTERNAL SERVER ERROR: Неизвестная ошибка сервера.

        Notes
        -----
        В `Headers` ответа при 503 ошибке вкладывается `"Retry-After": "120"`,
        т.е. просьба повторить запрос через 120 секунд.
        """
        try:
            response = await self.model_repo.health_check()
        except RpcError as e:
            match e.args[0].code:
                case StatusCode.UNAVAILABLE:
                    raise HTTPException(
                        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                        detail="Соединение с моделью не установлено.",
                        headers={"Retry-After": "120"},
                    )
                case _:
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail="Неизвестная ошибка.",
                    )

        return StandardResponse(message=response.message)

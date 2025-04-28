from fastapi import status
from grpc import RpcError, StatusCode

from repositories.model_repository import RecognitionModelRepository
from schemas.v1.responses import StandardResponse


class RecognitionModelService:
    def __init__(self, recognition_model_repo: RecognitionModelRepository):
        self.model_repo: RecognitionModelRepository = recognition_model_repo

    async def health_check(self):
        try:
            response = await self.model_repo.health_check()

            return StandardResponse(message=response.message)
        except RpcError as e:
            if e.args[0].code == StatusCode.UNAVAILABLE:
                return StandardResponse(
                    code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    message="Соединение с моделью не установлено.",
                )

        return StandardResponse(
            code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="Неизвестная ошибка."
        )

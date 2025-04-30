from fastapi import status, HTTPException
from grpc import RpcError, StatusCode

from repositories.model_repository import RecognitionModelRepository
from schemas.v1.responses import StandardResponse


class RecognitionModelService:
    def __init__(self, model_repo: RecognitionModelRepository):
        self.model_repo: RecognitionModelRepository = model_repo

    async def health_check(self) -> StandardResponse:
        try:
            response = await self.model_repo.health_check()

            return StandardResponse(message=response.message)
        except RpcError as e:
            if e.args[0].code == StatusCode.UNAVAILABLE:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Соединение с моделью не установлено.",
                    headers={"Retry-After": "120"},
                )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Неизвестная ошибка.",
        )

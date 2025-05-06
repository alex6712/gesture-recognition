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

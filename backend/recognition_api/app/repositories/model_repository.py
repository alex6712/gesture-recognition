from app.interservice_grpc.generated import recognition_model_pb2

from app.interservice_grpc.stubs import RecognitionModelStub


class RecognitionModelRepository:
    """Репозиторий для работы с моделью распознавания через gRPC.

    Класс предоставляет интерфейс для взаимодействия с сервисом распознавания
    через gRPC stub. Инкапсулирует логику вызова удаленных методов.

    Attributes
    ----------
    grpc_stub : RecognitionModelStub
        gRPC stub для взаимодействия с сервисом распознавания.

    Methods
    -------
    health_check()
        Проверка доступности сервиса распознавания.
    """

    def __init__(self, grpc_stub: RecognitionModelStub):
        self.grpc_stub: RecognitionModelStub = grpc_stub

    async def health_check(self) -> recognition_model_pb2.StandardResponse:  # noqa
        """Проверка доступности сервиса распознавания.

        Асинхронный метод, который проверяет доступность сервиса распознавания
        через gRPC вызов health check.

        Returns
        -------
        response : recognition_model_pb2.StandardResponse
            Ответ от сервиса распознавания.
        """
        return await self.grpc_stub.health_check()

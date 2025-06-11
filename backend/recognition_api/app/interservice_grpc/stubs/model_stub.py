import grpc
from app.interservice_grpc.generated.v1 import (
    recognition_model_pb2,
    recognition_model_pb2_grpc,
)


class RecognitionModelStub:
    """Класс gRPC-клиента.

    Является самым нижним слоем связи приложения с gRPC-сервером модели машинного обучения.

    Attributes
    ----------
    stub : recognition_model_pb2_grpc.RecognitionModelStub
        Исполнитель запросов.

    Methods
    -------
    health_check()
        Проверка работоспособности модели.
    """

    def __init__(self, host: str, port: int):
        self.stub = recognition_model_pb2_grpc.RecognitionModelStub(
            grpc.insecure_channel(f"{host}:{port}")
        )

    async def health_check(self) -> recognition_model_pb2.StandardResponse:  # noqa
        """Получение ответа от gRPC-сервера модели.

        Собирает gRPC-запрос (в данном случае пустой), возвращает
        ответ о работоспособности модели.

        Returns
        -------
        response : recognition_model_pb2.StandardResponse
            Ответ о работоспособности модели.
        """
        request = recognition_model_pb2.EmptyRequest()  # noqa
        return self.stub.HealthCheck(request)

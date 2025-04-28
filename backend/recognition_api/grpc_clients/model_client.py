from typing import TYPE_CHECKING

import grpc
from generated_grpc.recognition_model import (
    recognition_model_pb2,
    recognition_model_pb2_grpc,
)

if TYPE_CHECKING:
    from grpc import Channel


class RecognitionModelClient:
    """Класс gRPC-клиента.

    Является самым нижним слоем связи приложения с gRPC-сервером модели машинного обучения.

    Attributes
    ----------
    channel : Channel
        Канал связи с gRPC-сервером.
    stub : recognition_model_pb2_grpc.RecognitionModelStub
        Исполнитель запросов.

    Methods
    -------
    health_check()
        Проверка работоспособности модели.
    """

    def __init__(self, host: str, port: int):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = recognition_model_pb2_grpc.RecognitionModelStub(self.channel)

    async def health_check(self):
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

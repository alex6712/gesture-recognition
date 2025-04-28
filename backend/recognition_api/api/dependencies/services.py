from grpc_clients import RecognitionModelClient
from repositories import RecognitionModelRepository
from services import RecognitionModelService


async def get_model_service():
    """Создаёт объект сервисного слоя обслуживания gRPC сервера модели машинного обучения.

    Создаёт клиент gRPC-сервера, его обёртку в виде паттерна Repository, конструирует
    объект сервисного слоя и возвращает его.

    Используется как зависимость для endpoint, которые обращаются
    к модели.

    Returns
    -------
    service : RecognitionModelService
        Объект сервисного слоя.
    """
    model_client: RecognitionModelClient = RecognitionModelClient(
        host="recognition_model", port=50051
    )
    model_repository: RecognitionModelRepository = RecognitionModelRepository(
        model_client
    )

    return RecognitionModelService(model_repository)

from grpc_clients.model_client import RecognitionModelClient


class RecognitionModelRepository:
    def __init__(self, grpc_client: RecognitionModelClient):
        self.grpc_client = grpc_client

    async def health_check(self):
        return await self.grpc_client.health_check()

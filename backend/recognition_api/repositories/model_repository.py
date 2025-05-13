from interservice_grpc.stubs.model_stub import RecognitionModelStub


class RecognitionModelRepository:
    def __init__(self, grpc_client: RecognitionModelStub):
        self.grpc_client = grpc_client

    async def health_check(self):
        return await self.grpc_client.health_check()

from app.interservice_grpc.stubs import RecognitionModelStub


class RecognitionModelRepository:
    def __init__(self, grpc_stub: RecognitionModelStub):
        self.grpc_stub: RecognitionModelStub = grpc_stub

    async def health_check(self):
        return await self.grpc_stub.health_check()

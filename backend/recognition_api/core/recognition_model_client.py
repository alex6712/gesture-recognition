from functools import lru_cache

import grpc
from generated_grpc.recognition_model import (
    recognition_model_pb2,
    recognition_model_pb2_grpc,
)


class RecognitionModelClient:
    def __init__(self, host: str = "recognition_model", port: int = 50051):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = recognition_model_pb2_grpc.RecognitionModelStub(self.channel)

    def healthcheck(self) -> dict:
        request = recognition_model_pb2.EmptyRequest()
        response = self.stub.HealthCheck(request)

        return {"message": response.message}


@lru_cache()
def get_recognition_model_client() -> RecognitionModelClient:
    return RecognitionModelClient()

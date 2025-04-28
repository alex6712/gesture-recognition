from concurrent import futures

import grpc
from generated_grpc.recognition_model import (
    recognition_model_pb2,
    recognition_model_pb2_grpc,
)


class RecognitionModel(recognition_model_pb2_grpc.RecognitionModelServicer):
    def HealthCheck(self, request, context):
        return recognition_model_pb2.StandardResponse(message="Model works!")  # noqa


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    recognition_model_pb2_grpc.add_RecognitionModelServicer_to_server(
        RecognitionModel(), server
    )

    server.add_insecure_port("[::]:50051")
    server.start()

    print("gRPC server running on port 50051")

    server.wait_for_termination()

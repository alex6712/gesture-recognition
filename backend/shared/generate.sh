#!/bin/bash

python -m grpc_tools.protoc -I./proto --python_out=./generated_grpc/recognition_model --grpc_python_out=./generated_grpc/recognition_model ./proto/recognition_model.proto

# Фикс импортов для Python
sed -i 's/import recognition_model_pb2 as recognition__model__pb2/from generated_grpc.recognition_model import recognition_model_pb2 as recognition__model__pb2/' ./generated_grpc/recognition_model/recognition_model_pb2_grpc.py

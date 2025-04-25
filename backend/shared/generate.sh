#!/bin/bash

$(poetry env activate)

mkdir -p ./generated_grpc
touch ./generated_grpc/__init__.py

for proto_file in ./proto/*.proto; do
  service_name=$(basename "$proto_file" .proto)

  output_dir="./generated_grpc/${service_name}"
  mkdir -p "$output_dir"
  touch "${output_dir}/__init__.py"

  python -m grpc_tools.protoc \
    -I./proto \
    --python_out="$output_dir" \
    --grpc_python_out="$output_dir" \
    "$proto_file"

  generated_grpc_file="${output_dir}/${service_name}_pb2_grpc.py"
  if [ -f "$generated_grpc_file" ]; then
    sed -i "s/import ${service_name}_pb2 as ${service_name//_/__}__pb2/from generated_grpc.${service_name} import ${service_name}_pb2 as ${service_name//_/__}__pb2/" "$generated_grpc_file"
  fi

  echo "Обработан сервис: $service_name"
done

echo "Все .proto файлы обработаны!"

ARG DEPENDENCY_IMAGE=ghcr.io/fengelniederhammer/lapis-silo-dependencies:latest

FROM $DEPENDENCY_IMAGE AS builder

COPY . ./

RUN  \
    python3 ./build_with_conan.py --release --parallel 4\
    && cp build/Release/silo_test . \
    && cp build/Release/silo .


FROM ubuntu:24.04 AS server

WORKDIR /app
COPY docker_default_preprocessing_config.yaml ./default_preprocessing_config.yaml
COPY docker_runtime_config.yaml ./default_runtime_config.yaml
COPY --from=builder /src/silo ./

EXPOSE 8081

ENTRYPOINT ["./silo"]

ENV SILO_PREPROCESSING_CONFIG="/app/preprocessing_config.yaml"
ENV SILO_DEFAULT_PREPROCESSING_CONFIG="/app/default_preprocessing_config.yaml"
ENV SILO_DEFAULT_RUNTIME_CONFIG="/app/default_runtime_config.yaml"

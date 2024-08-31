#!/bin/bash

# Use multiple -f flags to include all service-specific and infrastructure Compose files
docker compose -f docker-compose.yml \
               -f ../infra/api-gateway/docker-compose.yml \
               -f ../services/iam-service/docker-compose.yml \
               up -d --build
#               -f ../services/media-service/docker-compose.yml \
#               -f ../services/ocr-service/docker-compose.yml \
#               -f ../infra/efk-stack/docker-compose.yml \
#               -f ../client/docker-compose.yml \



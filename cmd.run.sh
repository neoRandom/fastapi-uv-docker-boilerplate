#!/bin/bash

docker compose -f compose.yaml -f compose-tools.yaml up -d
docker compose alpha watch

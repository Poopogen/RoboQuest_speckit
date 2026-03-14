#!/usr/bin/env bash
set -euo pipefail

docker compose -f infra/docker-compose.yml up -d
uvicorn backend.api_gateway.app.main:app --reload &
API_PID=$!

python vr-client/simulator/run_sim.py --session

kill "$API_PID"

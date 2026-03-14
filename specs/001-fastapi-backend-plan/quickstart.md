# Quickstart — FastAPI Backend + XR Integration Platform

## Prerequisites

- Python 3.11 + Poetry
- Docker (Postgres, Redis, Qdrant, MinIO)
- ROS2 Humble + Gazebo

## Environment Setup

```bash
poetry install
```

```bash
docker compose -f infra/docker-compose.yml up -d
```

## Run API Gateway

```bash
uvicorn backend.api_gateway.app.main:app --reload
```

## Run ROS2 Bridge (Simulation)

```bash
export ROS_SIMULATION=true
ros2 run ros2_bridge dispatch_node
```

## Run VR Simulator

```bash
python vr-client/simulator/run_sim.py --session
```

## Tests

```bash
pytest tests/unit
pytest tests/integration
```

## Observability Stack

- Start OpenTelemetry collector + Tempo + Grafana via docker compose (optional).
- Ensure OTLP endpoint is configured in `backend/common/telemetry/otel.py`.

## End-to-End Flow

1. Start services + ROS2 bridge.
2. Run VR simulator to emit session + scan.
3. Verify session persisted in Postgres and events in Redis.
4. Dispatch task created and ROS2 telemetry returned.

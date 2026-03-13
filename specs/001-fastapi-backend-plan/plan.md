# Implementation Plan: FastAPI Backend + XR Integration Platform

**Branch**: `001-fastapi-backend-plan` | **Date**: 2026-03-13 | **Spec**: [`spec.md`](specs/001-fastapi-backend-plan/spec.md)
**Input**: Feature specification synthesized from `/specs/api-gateway/spec.md`, `/specs/backend-services/spec.md`, `/specs/data-layer/spec.md`, `/specs/data-agent-pipelines/spec.md`, `/specs/robot-layer/spec.md`, `/specs/game-layer/spec.md`, `/specs/vr-client/spec.md`, `/specs/ai-layer/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

Deliver a cohesive XR-to-robot control platform by standing up a FastAPI-based gateway and backend services, persistent data stores (PostgreSQL, Redis, Qdrant, dataset artifacts), ROS2 + Gazebo robot simulation, and a VR/game client simulator that emits gameplay events and validates backend integration. Each layer must expose contracts, implement schema/storage policies, provide mocks for hardware-less environments, and meet latency/observability targets defined across the specs.

**Phase 1 Preparation**: Document consolidated data entities (PlayerSession, VREvent, EnvironmentScan, DispatchTask, RobotState, SceneEmbedding, DatasetArtifact) in `data-model.md`, define REST/WebSocket/ROS2 contract files under `contracts/` (API gateway endpoints, backend service schemas, VR event schema, ROS2 topic/action definitions), and author `quickstart.md` covering environment setup (Python 3.11 + Poetry, Postgres/Redis/Qdrant/MinIO containers, ROS2 Humble workspace, Unity client build) plus canonical test commands.

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python 3.11 for API/data services, ROS2 Humble (Python/C++) for bridge/navigation (NEEDS CLARIFICATION on ROS2 node language split), Unity C# for VR client simulator (scope NEEDS CLARIFICATION)  
**Primary Dependencies**: FastAPI, Pydantic v2, SQLAlchemy 2.x + Alembic, Redis asyncio client, Qdrant client, Uvicorn, pytest + pytest-asyncio, ROS2 rclpy/rclcpp, Nav2, Gazebo, TurtleBot3 packages, Unity OpenXR SDK (sim client)  
**Storage**: PostgreSQL 15, Redis 7, Qdrant 1.7+, dataset storage (NEEDS CLARIFICATION if using MinIO/S3 vs local filesystem)  
**Testing**: pytest/unit/integration, FastAPI TestClient, contract tests per spec, ROS2 launch tests + Gazebo scenarios, VR simulator harness, Qdrant vector op tests  
**Target Platform**: Linux (Ubuntu 22.04) servers + ROS2/Gazebo workstation, VR simulator on Linux/Windows  
**Project Type**: Distributed backend services + robotics simulation + VR client stack  
**Performance Goals**: WebSocket ACK <150 ms p95, REST session read <200 ms p95, backend dispatch <2 s p95, Redis cache hit latency <50 ms, embedding query <500 ms p95, ROS2 telemetry <500 ms, VR retry success ≤3 attempts  
**Constraints**: JWT auth enforcement, rate limiting/backpressure, Nav2 collision avoidance ≥98%, dataset retention 30 days, structured logs/traces, fallback simulation when hardware unavailable  
**Scale/Scope**: ≥10k events/min ingestion, 50 concurrent dispatch tasks, multi-game plugin integration, multi-session VR + environment scans, orchestration gates across planner/coder/tool-runner/reviewer

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ⭕ Code quality gates defined: NEEDS CLARIFICATION on combined Ruff/mypy + ROS2 lint + Unity lint coverage.
- ⭕ Test benchmarks defined: need explicit mapping of pytest suites, ROS2 launch, Gazebo, VR sim, and vector store tests.
- ⭕ Mixed-reality UX parity checklist prepared: tactile mapping + fallback cues must be documented.
- ✅ Performance budgets defined (per Technical Context; instrumentation plan pending).
- ⭕ Observability plan defined: NEEDS CLARIFICATION on tracing/log aggregation stack across services/ROS2/VR.

## Project Structure

### Documentation (this feature)

```text
specs/001-fastapi-backend-plan/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (completed)
├── data-model.md        # Phase 1: entity definitions + relationships
├── quickstart.md        # Phase 1: env setup, services bootstrapping, test matrix
├── contracts/           # Phase 1: 
│   ├── api-gateway.md       # REST/WebSocket contract + auth/rate limits
│   ├── backend-services.md  # Game/Object Mapping/Robot Dispatcher APIs
│   ├── data-layer.md        # PostgreSQL schema + Redis/Qdrant access patterns
│   ├── robot-layer.md       # ROS2 topics/actions interfaces
│   └── vr-game.md           # VR event schema + game plugin contract
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
backend/
├── api_gateway/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── schemas/
│   │   └── services/
│   └── tests/
├── services/
│   ├── game_service/
│   ├── object_mapping/
│   ├── robot_dispatcher/
│   ├── environment_analyzer/
│   └── matchmaking/
├── data_layer/
│   ├── models/
│   ├── repositories/
│   ├── migrations/
│   └── tests/
└── common/
    ├── config/
    ├── telemetry/
    └── clients/

robotics/
├── ros2_bridge/
├── nav2_launch/
├── gazebo_worlds/
└── tests/

vr-client/
├── simulator/
├── event_fixtures/
└── tests/

tests/
├── unit/
├── integration/
├── contract/
└── simulation/
```

**Structure Decision**: Multi-root layout ensures backend services, robotics integration, VR simulator, and cross-cutting tests live in their own packages while sharing `common/` modules. This mirrors the multi-layer specs and simplifies CI + observability wiring.

### Phase 1 Deliverable Plan

1. **Data Model (`data-model.md`)**
   - Capture canonical entities spanning VR, backend, data, robot, and AI layers (PlayerSession, VREvent, EnvironmentScan, DispatchTask, RobotState, SceneEmbedding, DatasetArtifact, WorkflowGate).
   - Include field definitions, validation rules, relationships (e.g., DispatchTask ↔ RobotState, EnvironmentScan ↔ SceneEmbedding/Qdrant vector ID), and lifecycle notes (creation, updates, retention policies).
   - Reflect caching/persistence split (Redis vs PostgreSQL) and vector metadata (Qdrant collections) derived from research decisions.

2. **Contracts Directory (`contracts/`)**
   - **api-gateway.md**: REST endpoints (/sessions, /robots, /mappings) with request/response schemas, JWT scopes, rate-limits, and WebSocket event schema (ack semantics, backpressure signals).
   - **backend-services.md**: Service-to-service contracts (Game Service event normalization, Object Mapping request/response, Robot Dispatcher queue interface, Matchmaking inputs/outputs), plus Celery/Redis queue naming and timeout/retry policies.
   - **data-layer.md**: PostgreSQL schema tables, Redis key patterns, Qdrant collection schema (vector size, payload structure), MinIO bucket layout, and data retention policies.
   - **robot-layer.md**: ROS2 topics/actions (goal_pose, telemetry, battery_status), message schemas, QoS policies, simulation toggles, and bridge service API.
   - **vr-game.md**: VR event schema, environment scan payload format, coordinate alignment data (transform matrices), plugin rule contract, and simulator message coverage.

3. **Quickstart (`quickstart.md`)**
   - Environment setup instructions (Python 3.11 + Poetry, Docker compose for Postgres/Redis/Qdrant/MinIO, ROS2 Humble workspace, Unity project requirements).
   - Instructions to run FastAPI/Uvicorn, background workers, ROS2 bridge, Gazebo simulation, VR simulator harness, and Unity client in simulator mode.
   - Command list for linting/tests (Ruff, mypy, pytest, ros2 test, Unity Test Runner) and observability bootstrap (OpenTelemetry collector + Tempo/Prometheus/Grafana/Loki stack).
   - Sample workflow: ingest environment scan → run Object Mapping → dispatch simulated robot via Gazebo.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| TBD | Populate only if gates remain unmet after Phase 1 | N/A |

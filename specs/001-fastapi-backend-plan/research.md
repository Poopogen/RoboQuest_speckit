# Phase 0 Research — 001-fastapi-backend-plan

## 1. ROS2 Node Language Split
- **Decision**: Implement the REST/WebSocket→ROS2 bridge, Robot Dispatcher client, and telemetry fan-out in **rclpy** for tight FastAPI integration, while leveraging upstream **Nav2/TurtleBot3 rclcpp nodes** unchanged for navigation/execution.
- **Rationale**: Python bridge keeps serialization, Redis/Qdrant access, and FastAPI dependency graph in one runtime, while Nav2 already depends on performant C++ nodes maintained by the ROS2 community. This satisfies RB-FR-001/002/004 without re-authoring nav stack logic.
- **Alternatives considered**: (a) Rewrite bridge + Nav stack in rclcpp for uniformity—rejected due to slower iteration and duplicating stable Nav2 packages. (b) Pure rclpy stack—rejected because Nav2 features (behavior tree navigator, planners) are primarily C++.

## 2. VR Simulator Scope & Tooling
- **Decision**: Maintain a Unity/OpenXR client for interaction parity (per Platform Standards) and add a **Python-based headless simulator** that reuses the shared event schema to drive CI tests against FastAPI/ROS2 pipelines.
- **Rationale**: Unity client ensures tactile cues, coordinate alignment, and UX assets match production (VR-FR-001..006). Python harness enables deterministic integration tests without Unity runtime in CI.
- **Alternatives considered**: (a) Unity-only testing—rejected; too heavy for automated pipelines. (b) Pure Python mock client—rejected; would miss XR UX parity requirements.

## 3. Dataset Artifact Storage Backend
- **Decision**: Use **MinIO (S3-compatible object storage)** deployed alongside Postgres/Redis/Qdrant for raw scans, telemetry logs, and dataset versions, with lifecycle policies enforcing 30-day retention.
- **Rationale**: Aligns with DL-FR-004/005 and DP-FR-003 by offering scalable object storage w/ versioning metadata while staying self-hostable for dev. MinIO integrates with Python SDKs and ROS2 bag uploads.
- **Alternatives considered**: (a) Local filesystem—rejected for poor scalability and lack of metadata/version APIs. (b) Direct cloud S3 dependency—deferred to later to keep on-prem dev reproducible.

## 4. Linting & Static Analysis Coverage
- **Decision**: Adopt a multi-layer gate: `ruff + mypy` for FastAPI/services, `pytest --maxfail=1 -n auto` w/ `pytest-asyncio`, `ros2 test` + `ament_lint_auto` for ROS2 packages, `Unity Test Runner` for VR client, and markdown/spec linting via `markdownlint`.
- **Rationale**: Meets Constitution §I and Template gate by covering every language/runtime while keeping tooling aligned with existing communities (FastAPI, ROS2, Unity). Ensures automated enforcement before merge.
- **Alternatives considered**: (a) Flake8 instead of Ruff—rejected due to Ruff’s superset coverage and speed. (b) Skipping Unity tests until hardware available—rejected; UX parity requires automated coverage now.

## 5. Test Benchmarks & Suite Mapping
- **Decision**: Define four tiers: (1) FastAPI unit/contract tests (pytest + httpx TestClient); (2) Data-layer integration tests (pytest + dockerized Postgres/Redis/Qdrant); (3) ROS2/Gazebo launch tests validating goal dispatch + telemetry loops; (4) VR/Backend end-to-end using Unity playmode tests + Python simulator to assert dispatch acknowledgements within SLAs.
- **Rationale**: Fulfills Constitution §II and spec success criteria (API SC-001, Backend SC-001..005, VR SC-001..006, Robot SC-001..005). Each suite targets a measurable SLA (latency, queue depth, collision avoidance, telemetry interval).
- **Alternatives considered**: (a) Collapse tests into a single e2e suite—rejected; lacks isolation and violates “independently testable” requirement. (b) Defer ROS2 simulation until hardware—rejected; specs require simulation fallback.

## 6. Mixed-Reality UX Parity Checklist
- **Decision**: Track per-story tactile cues: (a) WebSocket event dispatch UI feedback (<50 ms); (b) Dispatch status + tactile mapping overlay; (c) Environment scan progress + mapping suggestions; (d) Coordinate alignment guidance (marker detection + transform success); (e) Robot delivery acknowledgement (visual + optional haptic). Checklist stored in repo (`docs/ux-parity.md`) and must be completed per PR.
- **Rationale**: Satisfies Constitution §III and VR spec requirements (VR-FR-004, SC-004/006). Provides reviewers a concrete list to verify parity across Unity + simulator logs.
- **Alternatives considered**: (a) Manual QA only—rejected due to lack of automation and governance compliance. (b) Limiting checklist to tactile cues—rejected; visual/audio cues also affect immersion.

## 7. Observability Stack
- **Decision**: Standardize on **OpenTelemetry** for tracing/metrics (FastAPI + ROS2 bridge via otel exporters) sending OTLP to **Tempo** (traces) and **Prometheus/Grafana** (metrics). Structured JSON logs shipped via **Loki** (or ELK) with correlation IDs across VR, backend, and robot layers. ROS2 nodes emit telemetry via `ros2_tracing` instrumentation feeding the same OTLP collector. VR simulator logs include session IDs to join traces.
- **Rationale**: Delivers Constitution §IV-V requirements and gives a single pipeline for latency budgets (VR↔backend, backend↔robot) plus dataset ingestion auditing. OpenTelemetry clients exist for Python, ROS2 (via tracing bridge), and Unity (OTLP exporter), minimizing custom plumbing.
- **Alternatives considered**: (a) Custom logging only—rejected; lacks distributed tracing/metrics correlation. (b) Proprietary APM—rejected for portability and cost reasons in early development.

---
All clarifications above feed back into the Technical Context/Constitution Check and unblock Phase 1 deliverables (data-model, contracts, quickstart).

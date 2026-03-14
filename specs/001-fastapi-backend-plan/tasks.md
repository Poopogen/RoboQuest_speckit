---

description: "Task list for FastAPI Backend + XR Integration Platform"
---

# Tasks: FastAPI Backend + XR Integration Platform

**Input**: Design documents from `/specs/001-fastapi-backend-plan/`
**Prerequisites**: plan.md (present), research.md (present), spec.md (missing), data-model.md (to be created), contracts/ (to be created), quickstart.md (to be created)

**Assumptions**:
- `/specs/001-fastapi-backend-plan/spec.md` is missing; user stories are inferred from [`plans/system-spec-plan.md`](plans/system-spec-plan.md:1), [`specs/001-fastapi-backend-plan/plan.md`](specs/001-fastapi-backend-plan/plan.md:1), and [`specs/001-fastapi-backend-plan/research.md`](specs/001-fastapi-backend-plan/research.md:1).
- `.specify/scripts/bash/check-prerequisites.sh --json` reported AVAILABLE_DOCS=["research.md"], but `plan.md` exists and is used as authoritative input.

**Tests**: Not explicitly requested; test tasks are omitted. Independent test criteria are listed per user story.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and missing design artifacts required to drive implementation.

- [x] T001 Create consolidated entity definitions in specs/001-fastapi-backend-plan/data-model.md
- [x] T002 Create API gateway contract in specs/001-fastapi-backend-plan/contracts/api-gateway.md
- [x] T003 Create backend services contract in specs/001-fastapi-backend-plan/contracts/backend-services.md
- [x] T004 Create data layer contract in specs/001-fastapi-backend-plan/contracts/data-layer.md
- [x] T005 Create robot layer contract in specs/001-fastapi-backend-plan/contracts/robot-layer.md
- [x] T006 Create VR/game contract in specs/001-fastapi-backend-plan/contracts/vr-game.md
- [x] T007 Create environment setup guide in specs/001-fastapi-backend-plan/quickstart.md
- [x] T008 [P] Initialize FastAPI entrypoint in backend/api_gateway/app/main.py
- [x] T009 [P] Add base package scaffolds in backend/common/config/__init__.py
- [x] T010 [P] Add telemetry scaffold in backend/common/telemetry/__init__.py
- [x] T011 [P] Add client wrappers scaffold in backend/common/clients/__init__.py
- [x] T012 [P] Create ROS2 bridge package scaffold in robotics/ros2_bridge/__init__.py
- [x] T013 [P] Create VR simulator scaffold in vr-client/simulator/__init__.py
- [x] T014 [P] Add root test folders in tests/unit/.gitkeep

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

- [x] T015 Implement environment config loader in backend/common/config/settings.py
- [x] T016 [P] Implement JWT auth utilities in backend/common/security/jwt.py
- [x] T017 [P] Implement rate limiting middleware in backend/api_gateway/app/middleware/rate_limit.py
- [x] T018 Implement shared exception handlers in backend/api_gateway/app/middleware/errors.py
- [x] T019 Implement OpenTelemetry setup in backend/common/telemetry/otel.py
- [x] T020 Implement Postgres engine/session factory in backend/data_layer/db/session.py
- [x] T021 [P] Implement Redis client wrapper in backend/common/clients/redis_client.py
- [x] T022 [P] Implement Qdrant client wrapper in backend/common/clients/qdrant_client.py
- [x] T023 [P] Implement MinIO client wrapper in backend/common/clients/minio_client.py
- [x] T024 Create base SQLAlchemy models in backend/data_layer/models/base.py
- [x] T025 [P] Add PlayerSession model in backend/data_layer/models/player_session.py
- [x] T026 [P] Add EnvironmentScan model in backend/data_layer/models/environment_scan.py
- [x] T027 [P] Add DispatchTask model in backend/data_layer/models/dispatch_task.py
- [x] T028 [P] Add RobotState model in backend/data_layer/models/robot_state.py
- [x] T029 [P] Add SceneEmbedding model in backend/data_layer/models/scene_embedding.py
- [x] T030 [P] Add DatasetArtifact model in backend/data_layer/models/dataset_artifact.py
- [x] T031 Implement repository base in backend/data_layer/repositories/base.py
- [x] T032 [P] Implement PlayerSession repository in backend/data_layer/repositories/player_sessions.py
- [x] T033 [P] Implement EnvironmentScan repository in backend/data_layer/repositories/environment_scans.py
- [x] T034 [P] Implement DispatchTask repository in backend/data_layer/repositories/dispatch_tasks.py
- [x] T035 Implement ROS2 bridge configuration in robotics/ros2_bridge/config.py
- [x] T036 Implement VR simulator event schema loader in vr-client/simulator/event_schema.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel.

---

## Phase 3: VR Session Ingestion & Gateway Handshake (Priority: P1) 🎯 MVP

**Goal**: Ingest VR sessions/scans/events via REST/WebSocket, enforce JWT/rate limits, persist sessions, and acknowledge within SLA.

**Independent Test**: Run VR simulator to send a session + scan; verify ACK <150 ms and session persisted in Postgres/Redis with trace IDs.

- [x] T037 [P] [US1] Define session schemas in backend/api_gateway/app/schemas/sessions.py
- [x] T038 [P] [US1] Define VR event schemas in backend/api_gateway/app/schemas/vr_events.py
- [x] T039 [US1] Implement session REST routes in backend/api_gateway/app/routes/sessions.py
- [x] T040 [US1] Implement WebSocket handshake/ack in backend/api_gateway/app/routes/ws_sessions.py
- [x] T041 [US1] Implement session service in backend/api_gateway/app/services/session_service.py
- [x] T042 [US1] Implement session persistence in backend/data_layer/repositories/player_sessions.py
- [x] T043 [US1] Implement VR event ingestion pipeline in backend/api_gateway/app/services/vr_event_ingest.py
- [x] T044 [US1] Implement Redis stream publisher for events in backend/common/clients/redis_client.py
- [x] T045 [US1] Add UX parity checklist updates in docs/ux-parity.md

**Checkpoint**: User Story 1 functional and independently testable.

---

## Phase 4: Object Mapping & Robot Dispatch (Priority: P1)

**Goal**: Normalize environment scans, map objects, enqueue dispatch tasks, and drive ROS2 Nav2 execution with telemetry.

**Independent Test**: Use Gazebo to execute a dispatch task; verify dispatch <2 s and telemetry interval <500 ms with collision avoidance ≥98%.

- [x] T046 [P] [US2] Implement mapping request schemas in backend/services/object_mapping/schemas.py
- [x] T047 [US2] Implement mapping service client in backend/services/object_mapping/client.py
- [x] T048 [US2] Implement dispatch queue interface in backend/services/robot_dispatcher/queue.py
- [x] T049 [US2] Implement dispatch task creator in backend/services/robot_dispatcher/service.py
- [x] T050 [US2] Implement ROS2 dispatch node in robotics/ros2_bridge/dispatch_node.py
- [x] T051 [US2] Implement ROS2 telemetry fan-out in robotics/ros2_bridge/telemetry_node.py
- [x] T052 [US2] Add Gazebo launch configuration in robotics/nav2_launch/dispatch_sim.launch.py
- [x] T053 [US2] Implement dispatch task persistence in backend/data_layer/repositories/dispatch_tasks.py
- [x] T054 [US2] Wire object mapping flow in backend/services/object_mapping/handler.py

**Checkpoint**: User Story 2 functional and independently testable.

---

## Phase 5: Data + Observability Layer (Priority: P2)

**Goal**: Persist scans/embeddings/datasets in Postgres/Qdrant/MinIO and enable end-to-end observability.

**Independent Test**: Upload dataset artifacts to MinIO and query embeddings from Qdrant with traces visible in Tempo/Grafana.

- [x] T055 [P] [US3] Implement Qdrant collection setup in backend/common/clients/qdrant_client.py
- [x] T056 [US3] Implement embedding write/read service in backend/services/object_mapping/embeddings.py
- [x] T057 [US3] Implement MinIO dataset writer in backend/common/clients/minio_client.py
- [x] T058 [US3] Implement dataset retention job in data-agent-pipelines/retention/cleanup.py
- [x] T059 [US3] Implement OpenTelemetry exporter wiring in backend/common/telemetry/otel.py
- [x] T060 [US3] Add trace correlation IDs in backend/api_gateway/app/middleware/request_id.py
- [x] T061 [US3] Implement environment scan persistence in backend/data_layer/repositories/environment_scans.py
- [x] T062 [US3] Implement scene embedding persistence in backend/data_layer/repositories/scene_embeddings.py

**Checkpoint**: User Story 3 functional and independently testable.

---

## Phase 6: Quickstart & Orchestration (Priority: P3)

**Goal**: Provide developer workflow scripts, CI harnesses, and parity documentation for consistent end-to-end runs.

**Independent Test**: Follow quickstart to boot services and run simulator → mapping → dispatch flow end-to-end.

- [x] T063 [P] [US4] Add Docker compose stack in infra/docker-compose.yml
- [x] T064 [US4] Implement CI harness script in scripts/run-e2e-sim.sh
- [x] T065 [US4] Add VR simulator workflow runner in vr-client/simulator/run_sim.py
- [x] T066 [US4] Add ROS2 + Gazebo smoke runner in robotics/tests/run_sim_smoke.py
- [x] T067 [US4] Document end-to-end workflow in specs/001-fastapi-backend-plan/quickstart.md
- [x] T068 [US4] Finalize UX parity checklist results in docs/ux-parity.md

**Checkpoint**: User Story 4 functional and independently testable.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [ ] T069 [P] Harden security headers in backend/api_gateway/app/middleware/security.py
- [ ] T070 Refine error taxonomy in backend/common/errors.py
- [ ] T071 Performance tuning for WebSocket ACK in backend/api_gateway/app/routes/ws_sessions.py
- [ ] T072 [P] Add repository documentation in docs/architecture.md
- [ ] T073 Run quickstart validation updates in specs/001-fastapi-backend-plan/quickstart.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - no dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - integrates with US1 events but independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - can run parallel to US1/US2
- **User Story 4 (P3)**: Depends on US1/US2/US3 for end-to-end workflow

### Within Each User Story

- Schemas before services
- Services before routing/integration
- Core implementation before orchestration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- After Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models and repository tasks marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch schema tasks for User Story 1 together:
Task: "Define session schemas in backend/api_gateway/app/schemas/sessions.py"
Task: "Define VR event schemas in backend/api_gateway/app/schemas/vr_events.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Demo MVP if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Demo (MVP)
3. Add User Story 2 → Test independently → Demo
4. Add User Story 3 → Test independently → Demo
5. Add User Story 4 → End-to-end workflow validation

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. User Story 4 follows once US1–US3 are stable

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Avoid cross-story dependencies that break independence

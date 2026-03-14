## US1–US4 Test Coverage & Acceptance Verification

**Artifacts referenced**: [`specs/ai-layer/spec.md`](specs/ai-layer/spec.md:1), [`specs/001-fastapi-backend-plan/plan.md`](specs/001-fastapi-backend-plan/plan.md:1), [`specs/001-fastapi-backend-plan/tasks.md`](specs/001-fastapi-backend-plan/tasks.md:70)

### Coverage Table

| User Story | Test Authoring Tasks | Test Execution Tasks | Independent Acceptance Check | Status |
|---|---|---|---|---|
| US1 – VR Session Ingestion | [`T037–T039`](specs/001-fastapi-backend-plan/tasks.md:81) | [`T087–T089`](specs/001-fastapi-backend-plan/tasks.md:84) | [`T090`](specs/001-fastapi-backend-plan/tasks.md:87) | **CRITICAL** – unchecked; execution blocked per env note |
| US2 – Object Mapping & Dispatch | [`T049–T052`](specs/001-fastapi-backend-plan/tasks.md:113) | [`T091–T093`](specs/001-fastapi-backend-plan/tasks.md:117) | [`T094`](specs/001-fastapi-backend-plan/tasks.md:120) | **CRITICAL** – unchecked |
| US3 – Data & Observability | [`T062–T064`](specs/001-fastapi-backend-plan/tasks.md:146) | [`T095–T097`](specs/001-fastapi-backend-plan/tasks.md:149) | [`T098`](specs/001-fastapi-backend-plan/tasks.md:152) | **CRITICAL** – unchecked |
| US4 – Quickstart & Orchestration | [`T073–T075`](specs/001-fastapi-backend-plan/tasks.md:177) | [`T099–T101`](specs/001-fastapi-backend-plan/tasks.md:180) | [`T102`](specs/001-fastapi-backend-plan/tasks.md:183) | **CRITICAL** – unchecked |

### Observations

1. Every story has explicit TDD tasks and acceptance checks; no missing coverage items.
2. Execution note in [`tasks.md`](specs/001-fastapi-backend-plan/tasks.md:79) confirms pytest/ROS2 commands cannot run yet, leaving all execution/acceptance tasks unchecked. This violates the XR-to-Robot Test Benchmark requirement in [`constitution.md`](.specify/memory/constitution.md:20).

### Remediation Plan

1. Provision Python 3.11 + pip/pytest and ROS2/Gazebo as outlined in [`quickstart.md`](specs/001-fastapi-backend-plan/quickstart.md:1) to clear the environment blocker.
2. Execute US1 validation sequence: run T087–T089, then acceptance T090, recording pass/fail results.
3. Execute US2 validation sequence: run T091–T093 and acceptance T094.
4. Execute US3 validation sequence: run T095–T097 and acceptance T098.
5. Execute US4 validation sequence: run T099–T101 and acceptance T102.
6. Update [`tasks.md`](specs/001-fastapi-backend-plan/tasks.md:70) with actual outcomes before `/speckit.implement`.

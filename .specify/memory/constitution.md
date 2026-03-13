<!--
Sync Impact Report
- Version change: 0.0.0 → 0.1.0
- Modified principles: N/A (initial constitution)
- Added sections: Core Principles, Platform Execution Standards, Delivery Workflow & Quality Gates, Governance
- Removed sections: None
- Templates requiring updates: ✅ .specify/templates/plan-template.md, ✅ .specify/templates/spec-template.md, ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: TODO(RATIFICATION_DATE): original ratification date unknown
-->
# RoboQuest VR Constitution

## Core Principles

### I. Code Quality Discipline
All production code MUST meet linting, formatting, and static analysis gates before merge.
Modules MUST be cohesive, documented, and versioned with clear ownership and boundaries.
Refactors that reduce complexity are mandatory when introducing new cross-cutting behavior.
Rationale: Mixed-reality robotics demands predictable, maintainable code for safety and velocity.

### II. XR-to-Robot Test Benchmarks
Each user story MUST include unit tests plus integration tests spanning VR events,
backend dispatch, and ROS2 command flow. Hardware-in-loop or simulation tests are
required for robot control paths. Tests MUST fail before implementation and pass
before release. Rationale: Safety and correctness depend on verifiable end-to-end flows.

### III. Consistent Mixed-Reality UX
User interactions MUST preserve consistent tactile mapping, visual cues, and
feedback timing across devices and environments. UX changes MUST include parity
checks against baseline interactions and accessibility requirements.
Rationale: Mixed-reality immersion relies on predictable, cross-context behavior.

### IV. Performance & Reliability Metrics
Latency budgets MUST be defined and tracked for VR-to-backend (<150ms p95) and
backend-to-robot dispatch (<2s p95) paths. Services MUST expose p95/p99 metrics and
error budgets. Regressions require explicit approval and rollback plans.
Rationale: Real-time MR experiences fail without measurable performance guarantees.

### V. Data Integrity & Observability
Telemetry, sensor data, and event logs MUST be structured, time-synchronized, and
traceable across VR, backend, and robot layers. Critical flows MUST include audit
events and replayable traces. Rationale: Debugging and safety validation require
high-fidelity system observability.

## Platform Execution Standards

- Backend services MUST use FastAPI with documented REST and WebSocket contracts.
- Robot control MUST use ROS2 with a dedicated bridge service and simulation support.
- VR clients MUST use Unity/OpenXR with a shared event schema for game plugins.
- Data storage MUST support structured telemetry and vector search (e.g., Qdrant).
- Observability MUST include structured logs, traces, and metric dashboards for
  latency, error rates, and dispatch success.

## Delivery Workflow & Quality Gates

- Constitution Check is required before research, design, and implementation phases.
- Every PR MUST include: test evidence, UX parity checklist, and performance metrics.
- Cross-layer changes (VR ↔ backend ↔ robot) require end-to-end integration testing.
- Releases MUST include a rollback plan and monitored canary validation.

## Governance

- This constitution supersedes all other project practices and templates.
- Amendments require: rationale, impact analysis, version bump, and approval by
  the designated technical lead and product owner.
- Versioning policy follows semantic versioning (MAJOR for breaking governance
  changes, MINOR for new principles or sections, PATCH for clarifications).
- Compliance reviews occur every release and must reference DESIGN.md as the
  authoritative architecture guide.

**Version**: 0.1.0 | **Ratified**: TODO(RATIFICATION_DATE): original adoption date unknown | **Last Amended**: 2026-03-13

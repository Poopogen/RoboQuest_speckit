# Data Model — FastAPI Backend + XR Integration Platform

This document consolidates the canonical entities and relationships spanning the VR client, API gateway, backend services, data layer, and robot/AI subsystems.

## Entities

### PlayerSession

- **Purpose**: Root record for a VR gameplay session and its ingestion lifecycle.
- **Primary Key**: `id` (UUID)
- **Core Fields**
  - `user_id` (string) — Authenticated subject (JWT sub)
  - `status` (enum: `pending`, `active`, `ended`, `failed`)
  - `started_at` (datetime)
  - `ended_at` (datetime, nullable)
  - `client_version` (string)
  - `environment_id` (string, nullable)
  - `session_metadata` (json) — device, build, locale
- **Relationships**
  - 1→N with `VREvent`
  - 1→N with `EnvironmentScan`
  - 1→N with `DispatchTask`
  - 1→N with `RobotState`

### VREvent

- **Purpose**: Normalized event stream from the VR client (actions, telemetry, UI events).
- **Primary Key**: `id` (UUID)
- **Core Fields**
  - `session_id` (UUID, FK → PlayerSession)
  - `event_type` (string)
  - `event_time` (datetime)
  - `payload` (json)
  - `trace_id` (string, nullable)
- **Storage**
  - Hot path: Redis streams (`vr:events:{session_id}`)
  - Cold path: Postgres `vr_events` table (optional retention)

### EnvironmentScan

- **Purpose**: Captures spatial scan data emitted by the VR client or robot sensing.
- **Primary Key**: `id` (UUID)
- **Core Fields**
  - `session_id` (UUID, FK → PlayerSession)
  - `scan_type` (enum: `mesh`, `point_cloud`, `depth_map`)
  - `source` (enum: `vr_client`, `robot`)
  - `captured_at` (datetime)
  - `artifact_uri` (string, MinIO/S3 path)
  - `coordinate_frame` (string)
  - `metadata` (json)

### DispatchTask

- **Purpose**: Work item describing a robot action derived from mapping/dispatch.
- **Primary Key**: `id` (UUID)
- **Core Fields**
  - `session_id` (UUID, FK → PlayerSession)
  - `environment_scan_id` (UUID, FK → EnvironmentScan, nullable)
  - `robot_id` (string)
  - `target_pose` (json: position + orientation)
  - `status` (enum: `queued`, `sent`, `executing`, `completed`, `failed`)
  - `created_at` (datetime)
  - `updated_at` (datetime)
  - `failure_reason` (string, nullable)

### RobotState

- **Purpose**: Time-series snapshot of robot telemetry.
- **Primary Key**: `id` (UUID)
- **Core Fields**
  - `session_id` (UUID, FK → PlayerSession)
  - `robot_id` (string)
  - `state_time` (datetime)
  - `pose` (json)
  - `battery` (float)
  - `status` (string)
  - `telemetry` (json)

### SceneEmbedding

- **Purpose**: Vector representation of environment scans for retrieval.
- **Primary Key**: `id` (UUID)
- **Core Fields**
  - `environment_scan_id` (UUID, FK → EnvironmentScan)
  - `qdrant_collection` (string)
  - `qdrant_point_id` (string)
  - `embedding_dim` (int)
  - `created_at` (datetime)
  - `metadata` (json)

### DatasetArtifact

- **Purpose**: Raw or processed data bundle stored in MinIO.
- **Primary Key**: `id` (UUID)
- **Core Fields**
  - `session_id` (UUID, FK → PlayerSession)
  - `artifact_type` (enum: `scan`, `log`, `telemetry`, `dataset`)
  - `bucket` (string)
  - `object_key` (string)
  - `size_bytes` (int)
  - `checksum` (string)
  - `created_at` (datetime)

### WorkflowGate

- **Purpose**: Orchestration checkpoint to coordinate pipeline readiness.
- **Primary Key**: `id` (UUID)
- **Core Fields**
  - `name` (string)
  - `status` (enum: `open`, `blocked`, `completed`)
  - `updated_at` (datetime)
  - `details` (json)

## Relationships & Lifecycle

- `PlayerSession` is the root entity; all other entities attach by `session_id` where applicable.
- `EnvironmentScan` may exist before dispatch tasks; `SceneEmbedding` references scans post-processing.
- `DispatchTask` uses `RobotState` telemetry for success/failure evaluation.
- `DatasetArtifact` references raw scans and derived outputs, retained for 30 days (MinIO lifecycle policy).

## Storage & Retention

- **Postgres**: `player_sessions`, `environment_scans`, `dispatch_tasks`, `robot_states`, `scene_embeddings`, `dataset_artifacts`.
- **Redis**: session cache (`session:{id}`), event streams, rate limit buckets.
- **Qdrant**: `scene_embeddings` collection with payload metadata (session_id, scan_id, tags).
- **MinIO**: buckets per artifact type; 30-day lifecycle enforcement.

## Validation Notes

- All UUIDs are generated server-side.
- `event_time` and `captured_at` use UTC ISO-8601.
- `coordinate_frame` must match agreed transforms in `contracts/vr-game.md`.

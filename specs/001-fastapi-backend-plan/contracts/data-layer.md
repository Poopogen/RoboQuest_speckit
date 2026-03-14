# Data Layer Contract

## PostgreSQL Tables

- `player_sessions`
- `environment_scans`
- `dispatch_tasks`
- `robot_states`
- `scene_embeddings`
- `dataset_artifacts`

## Redis Keys

- Session cache: `session:{session_id}`
- Rate limit: `rate:{user_id}:{route}`
- Event stream: `vr:events:{session_id}`

## Qdrant

- Collection: `scene_embeddings`
- Payload: `session_id`, `scan_id`, `tags`, `created_at`
- Vector size: 768 (default; configurable)

## MinIO

- Buckets: `scans`, `datasets`, `telemetry`
- Object key: `{session_id}/{artifact_id}/{filename}`

## Retention

- MinIO lifecycle: 30 days
- Postgres: 180 days (configurable)
- Redis: 7 days (configurable)

# Backend Services Contract

## Game Service

- **Input**: Normalized VR events.
- **Output**: Gameplay-derived signals (object mapping requests, dispatch triggers).

## Object Mapping Service

- **Request**
  ```json
  {
    "session_id": "uuid",
    "scan_id": "uuid",
    "mapping_type": "semantic",
    "parameters": {"min_confidence": 0.8}
  }
  ```
- **Response**
  ```json
  {
    "mapping_id": "uuid",
    "status": "queued",
    "estimated_latency_ms": 800
  }
  ```

## Robot Dispatcher

- **Queue Name**: `robot.dispatch.tasks`
- **Message**
  ```json
  {
    "task_id": "uuid",
    "robot_id": "tb3-01",
    "target_pose": {"x": 0, "y": 0, "theta": 0},
    "session_id": "uuid"
  }
  ```

## Matchmaking Service (Future)

- Inputs: concurrent session capacity, robot availability, environment readiness.
- Outputs: session assignment with robot + environment ID.

## Timeouts/Retry

- Object mapping: 3 retries, exponential backoff (250ms → 2s).
- Dispatch: 5 retries, dead-letter after 3 minutes.

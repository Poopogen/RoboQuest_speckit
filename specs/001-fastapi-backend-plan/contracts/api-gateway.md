# API Gateway Contract

## Overview

The API gateway exposes REST + WebSocket endpoints for VR session ingestion, scan uploads, and robot dispatch signals. All endpoints require JWT auth unless noted.

## Auth & Rate Limits

- **JWT**: `Authorization: Bearer <token>`
- **Scopes**: `vr:session`, `vr:events`, `robot:dispatch`, `admin:read`
- **Rate Limits**:
  - REST: 60 req/min per user
  - WebSocket: 120 events/min per session

## REST Endpoints

### POST /sessions

- **Purpose**: Create a new player session.
- **Scope**: `vr:session`
- **Request**
  ```json
  {
    "client_version": "1.0.0",
    "environment_id": "lab-1",
    "session_metadata": {"device": "Quest3"}
  }
  ```
- **Response**
  ```json
  {
    "session_id": "uuid",
    "status": "active",
    "started_at": "2026-03-13T00:00:00Z"
  }
  ```

### GET /sessions/{session_id}

- **Purpose**: Read session status.
- **Scope**: `vr:session`

### POST /sessions/{session_id}/scans

- **Purpose**: Register a scan artifact.
- **Scope**: `vr:events`
- **Request**
  ```json
  {
    "scan_type": "mesh",
    "artifact_uri": "s3://scans/session/scan.glb",
    "coordinate_frame": "vr_world",
    "metadata": {"units": "meters"}
  }
  ```
- **Response**
  ```json
  {"scan_id": "uuid", "status": "received"}
  ```

### POST /dispatch

- **Purpose**: Enqueue a robot dispatch task.
- **Scope**: `robot:dispatch`

## WebSocket

### /ws/sessions/{session_id}

- **Purpose**: Bi-directional VR event streaming.
- **Handshake**: Send `{ "type": "hello", "trace_id": "..." }` → server responds with ack within 150ms.
- **Event Payload**
  ```json
  {
    "event_type": "object_selected",
    "event_time": "2026-03-13T00:00:00Z",
    "payload": {"object_id": "bin-12"}
  }
  ```
- **Ack**
  ```json
  {"type": "ack", "event_id": "uuid", "received_at": "..."}
  ```

## Error Responses

- 400: Validation error
- 401: Unauthorized
- 403: Forbidden (missing scope)
- 429: Rate limit exceeded
- 500: Internal error

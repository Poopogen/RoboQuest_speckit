# VR/Game Contract

## Event Schema

- Base fields: `event_type`, `event_time`, `payload`, `trace_id`
- All timestamps in UTC ISO-8601

## Environment Scan Payload

```json
{
  "scan_type": "mesh",
  "artifact_uri": "s3://scans/session/scan.glb",
  "coordinate_frame": "vr_world",
  "transform": {
    "position": [0, 0, 0],
    "rotation": [0, 0, 0, 1]
  },
  "metadata": {"units": "meters"}
}
```

## Coordinate Alignment

- VR world frame → robot map frame transform must be attached to each scan.
- Server validates transform presence and logs mismatches.

## Simulator Coverage

- Session start/stop
- Object selection
- Environment scan upload
- Dispatch request trigger

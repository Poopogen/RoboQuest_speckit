from backend.common.clients.redis_client import publish_event


def ingest_vr_event(session_id: str, event: dict) -> str:
    stream = f"vr:events:{session_id}"
    return publish_event(stream, event)

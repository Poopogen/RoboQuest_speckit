from fastapi import APIRouter, WebSocket

from backend.api_gateway.app.services.vr_event_ingest import ingest_vr_event

router = APIRouter(prefix="/ws/sessions", tags=["ws-sessions"])


@router.websocket("/{session_id}")
async def ws_session(websocket: WebSocket, session_id: str):
    await websocket.accept()
    hello = await websocket.receive_json()
    await websocket.send_json({"type": "ack", "received_at": hello.get("event_time")})
    while True:
        event = await websocket.receive_json()
        ingest_vr_event(session_id, event)
        await websocket.send_json({"type": "ack", "event_type": event.get("event_type")})

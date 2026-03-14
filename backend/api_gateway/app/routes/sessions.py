from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.api_gateway.app.schemas.sessions import SessionCreate, SessionResponse
from backend.api_gateway.app.services.session_service import SessionService
from backend.data_layer.db.session import SessionLocal

router = APIRouter(prefix="/sessions", tags=["sessions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("", response_model=SessionResponse)
def create_session(payload: SessionCreate, db: Session = Depends(get_db)):
    service = SessionService(db)
    session = service.create_session(
        user_id="anonymous",
        client_version=payload.client_version,
        environment_id=payload.environment_id,
        metadata=payload.session_metadata,
    )
    return SessionResponse(session_id=str(session.id), status=session.status, started_at=session.started_at)

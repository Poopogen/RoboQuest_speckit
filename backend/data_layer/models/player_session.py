import uuid

from sqlalchemy import Column, DateTime, JSON, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.data_layer.models.base import Base


class PlayerSession(Base):
    __tablename__ = "player_sessions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String, nullable=False)
    status = Column(String, nullable=False, default="active")
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    ended_at = Column(DateTime(timezone=True), nullable=True)
    client_version = Column(String, nullable=True)
    environment_id = Column(String, nullable=True)
    session_metadata = Column(JSON, nullable=True)

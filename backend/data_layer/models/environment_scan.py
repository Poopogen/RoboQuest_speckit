import uuid

from sqlalchemy import Column, DateTime, JSON, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.data_layer.models.base import Base


class EnvironmentScan(Base):
    __tablename__ = "environment_scans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), nullable=False)
    scan_type = Column(String, nullable=False)
    source = Column(String, nullable=False, default="vr_client")
    captured_at = Column(DateTime(timezone=True), server_default=func.now())
    artifact_uri = Column(String, nullable=False)
    coordinate_frame = Column(String, nullable=False)
    metadata = Column(JSON, nullable=True)

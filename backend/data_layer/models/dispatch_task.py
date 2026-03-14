import uuid

from sqlalchemy import Column, DateTime, JSON, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.data_layer.models.base import Base


class DispatchTask(Base):
    __tablename__ = "dispatch_tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), nullable=False)
    environment_scan_id = Column(UUID(as_uuid=True), nullable=True)
    robot_id = Column(String, nullable=False)
    target_pose = Column(JSON, nullable=False)
    status = Column(String, nullable=False, default="queued")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    failure_reason = Column(String, nullable=True)

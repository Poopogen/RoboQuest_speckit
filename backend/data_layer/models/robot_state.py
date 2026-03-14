import uuid

from sqlalchemy import Column, DateTime, JSON, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.data_layer.models.base import Base


class RobotState(Base):
    __tablename__ = "robot_states"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), nullable=False)
    robot_id = Column(String, nullable=False)
    state_time = Column(DateTime(timezone=True), server_default=func.now())
    pose = Column(JSON, nullable=True)
    battery = Column(String, nullable=True)
    status = Column(String, nullable=True)
    telemetry = Column(JSON, nullable=True)

import uuid

from sqlalchemy import Column, DateTime, JSON, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.data_layer.models.base import Base


class SceneEmbedding(Base):
    __tablename__ = "scene_embeddings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    environment_scan_id = Column(UUID(as_uuid=True), nullable=False)
    qdrant_collection = Column(String, nullable=False)
    qdrant_point_id = Column(String, nullable=False)
    embedding_dim = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    metadata = Column(JSON, nullable=True)

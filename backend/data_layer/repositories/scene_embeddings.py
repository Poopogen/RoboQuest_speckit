from sqlalchemy.orm import Session

from backend.data_layer.models.scene_embedding import SceneEmbedding
from backend.data_layer.repositories.base import Repository


class SceneEmbeddingRepository(Repository[SceneEmbedding]):
    def __init__(self, session: Session):
        super().__init__(session=session, model=SceneEmbedding)

    def create_embedding(self, environment_scan_id: str, qdrant_collection: str, qdrant_point_id: str, embedding_dim: int, metadata: dict | None):
        instance = SceneEmbedding(
            environment_scan_id=environment_scan_id,
            qdrant_collection=qdrant_collection,
            qdrant_point_id=qdrant_point_id,
            embedding_dim=embedding_dim,
            metadata=metadata,
        )
        return self.add(instance)

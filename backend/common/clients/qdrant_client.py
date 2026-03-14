from qdrant_client import QdrantClient
from qdrant_client.http import models

from backend.common.config.settings import get_settings


def get_qdrant_client() -> QdrantClient:
    settings = get_settings()
    return QdrantClient(url=settings.qdrant_url)


def ensure_scene_embeddings_collection(vector_size: int = 768) -> None:
    client = get_qdrant_client()
    collections = client.get_collections().collections
    if any(col.name == "scene_embeddings" for col in collections):
        return
    client.recreate_collection(
        collection_name="scene_embeddings",
        vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
    )

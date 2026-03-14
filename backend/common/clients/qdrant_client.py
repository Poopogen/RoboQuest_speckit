from qdrant_client import QdrantClient

from backend.common.config.settings import get_settings


def get_qdrant_client() -> QdrantClient:
    settings = get_settings()
    return QdrantClient(url=settings.qdrant_url)

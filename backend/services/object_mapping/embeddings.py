from backend.common.clients.qdrant_client import get_qdrant_client


def upsert_embedding(point_id: str, vector: list[float], payload: dict) -> None:
    client = get_qdrant_client()
    client.upsert(
        collection_name="scene_embeddings",
        points=[{"id": point_id, "vector": vector, "payload": payload}],
    )


def query_embeddings(vector: list[float], limit: int = 5):
    client = get_qdrant_client()
    return client.search(collection_name="scene_embeddings", query_vector=vector, limit=limit)

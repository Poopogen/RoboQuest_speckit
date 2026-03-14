from typing import Any

import redis

from backend.common.config.settings import get_settings


def get_redis_client() -> redis.Redis:
    settings = get_settings()
    return redis.from_url(settings.redis_url, decode_responses=True)


def publish_event(stream: str, payload: dict[str, Any]) -> str:
    client = get_redis_client()
    return client.xadd(stream, payload)

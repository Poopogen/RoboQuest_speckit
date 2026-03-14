import datetime
from typing import Any

import jwt

from backend.common.config.settings import get_settings


def encode_token(subject: str, expires_minutes: int = 60, scopes: list[str] | None = None) -> str:
    settings = get_settings()
    payload: dict[str, Any] = {
        "sub": subject,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_minutes),
        "scopes": scopes or [],
    }
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)


def decode_token(token: str) -> dict[str, Any]:
    settings = get_settings()
    return jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])

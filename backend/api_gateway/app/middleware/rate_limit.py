from collections import defaultdict
from datetime import datetime, timedelta

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from backend.common.config.settings import get_settings


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app) -> None:
        super().__init__(app)
        self._requests: dict[str, list[datetime]] = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        settings = get_settings()
        key = request.client.host if request.client else "anonymous"
        now = datetime.utcnow()
        window_start = now - timedelta(minutes=1)
        self._requests[key] = [t for t in self._requests[key] if t >= window_start]
        if len(self._requests[key]) >= settings.rate_limit_per_minute:
            return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})
        self._requests[key].append(now)
        return await call_next(request)

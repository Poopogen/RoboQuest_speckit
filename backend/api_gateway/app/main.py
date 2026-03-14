from fastapi import FastAPI

from backend.api_gateway.app.middleware.errors import add_exception_handlers
from backend.api_gateway.app.middleware.rate_limit import RateLimitMiddleware
from backend.api_gateway.app.routes.sessions import router as sessions_router
from backend.api_gateway.app.routes.ws_sessions import router as ws_sessions_router


def create_app() -> FastAPI:
    app = FastAPI(title="XR Integration Gateway")
    app.add_middleware(RateLimitMiddleware)
    app.include_router(sessions_router)
    app.include_router(ws_sessions_router)
    add_exception_handlers(app)
    return app


app = create_app()

from functools import lru_cache
from pydantic import BaseModel, Field


class Settings(BaseModel):
    app_name: str = "XR Integration Gateway"
    environment: str = Field(default="dev")
    database_url: str = Field(default="postgresql+psycopg://postgres:postgres@localhost:5432/xr")
    redis_url: str = Field(default="redis://localhost:6379/0")
    qdrant_url: str = Field(default="http://localhost:6333")
    minio_endpoint: str = Field(default="localhost:9000")
    minio_access_key: str = Field(default="minioadmin")
    minio_secret_key: str = Field(default="minioadmin")
    jwt_secret: str = Field(default="change-me")
    jwt_algorithm: str = Field(default="HS256")
    rate_limit_per_minute: int = Field(default=60)
    otel_endpoint: str = Field(default="http://localhost:4317")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

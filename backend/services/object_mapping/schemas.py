from pydantic import BaseModel


class MappingRequest(BaseModel):
    session_id: str
    scan_id: str
    mapping_type: str = "semantic"
    parameters: dict | None = None


class MappingResponse(BaseModel):
    mapping_id: str
    status: str
    estimated_latency_ms: int | None = None

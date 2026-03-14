from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SessionCreate(BaseModel):
    client_version: Optional[str] = None
    environment_id: Optional[str] = None
    session_metadata: Optional[dict] = None


class SessionResponse(BaseModel):
    session_id: str
    status: str
    started_at: datetime

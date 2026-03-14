from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


class VREvent(BaseModel):
    event_type: str
    event_time: datetime
    payload: dict[str, Any]
    trace_id: Optional[str] = None

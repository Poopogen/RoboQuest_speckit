import json
from pathlib import Path


def load_event_schema(path: str) -> dict:
    schema_path = Path(path)
    return json.loads(schema_path.read_text())

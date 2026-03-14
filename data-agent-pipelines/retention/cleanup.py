from datetime import datetime, timedelta


def should_expire(created_at: datetime, retention_days: int = 30) -> bool:
    return created_at < datetime.utcnow() - timedelta(days=retention_days)

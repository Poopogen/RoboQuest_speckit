from sqlalchemy.orm import Session

from backend.data_layer.repositories.player_sessions import PlayerSessionRepository


class SessionService:
    def __init__(self, session: Session):
        self.repository = PlayerSessionRepository(session)

    def create_session(self, user_id: str, client_version: str | None, environment_id: str | None, metadata: dict | None):
        return self.repository.create_session(user_id, client_version, environment_id, metadata)

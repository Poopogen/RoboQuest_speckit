from sqlalchemy.orm import Session

from backend.data_layer.models.player_session import PlayerSession
from backend.data_layer.repositories.base import Repository


class PlayerSessionRepository(Repository[PlayerSession]):
    def __init__(self, session: Session):
        super().__init__(session=session, model=PlayerSession)

    def create_session(self, user_id: str, client_version: str | None, environment_id: str | None, metadata: dict | None):
        instance = PlayerSession(
            user_id=user_id,
            client_version=client_version,
            environment_id=environment_id,
            session_metadata=metadata,
        )
        return self.add(instance)

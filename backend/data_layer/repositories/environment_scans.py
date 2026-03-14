from sqlalchemy.orm import Session

from backend.data_layer.models.environment_scan import EnvironmentScan
from backend.data_layer.repositories.base import Repository


class EnvironmentScanRepository(Repository[EnvironmentScan]):
    def __init__(self, session: Session):
        super().__init__(session=session, model=EnvironmentScan)

    def create_scan(self, session_id: str, scan_type: str, artifact_uri: str, coordinate_frame: str, metadata: dict | None):
        instance = EnvironmentScan(
            session_id=session_id,
            scan_type=scan_type,
            artifact_uri=artifact_uri,
            coordinate_frame=coordinate_frame,
            metadata=metadata,
        )
        return self.add(instance)

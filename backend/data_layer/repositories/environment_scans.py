from sqlalchemy.orm import Session

from backend.data_layer.models.environment_scan import EnvironmentScan
from backend.data_layer.repositories.base import Repository


class EnvironmentScanRepository(Repository[EnvironmentScan]):
    def __init__(self, session: Session):
        super().__init__(session=session, model=EnvironmentScan)

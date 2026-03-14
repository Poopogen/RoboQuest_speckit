from sqlalchemy.orm import Session

from backend.data_layer.models.dispatch_task import DispatchTask
from backend.data_layer.repositories.base import Repository


class DispatchTaskRepository(Repository[DispatchTask]):
    def __init__(self, session: Session):
        super().__init__(session=session, model=DispatchTask)

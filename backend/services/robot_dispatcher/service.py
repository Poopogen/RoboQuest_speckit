import uuid

from backend.services.robot_dispatcher.queue import DispatchQueue


class RobotDispatcherService:
    def __init__(self, queue: DispatchQueue) -> None:
        self.queue = queue

    def create_task(self, session_id: str, robot_id: str, target_pose: dict) -> dict:
        task = {
            "task_id": str(uuid.uuid4()),
            "session_id": session_id,
            "robot_id": robot_id,
            "target_pose": target_pose,
        }
        self.queue.enqueue(task)
        return task

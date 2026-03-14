from collections import deque


class DispatchQueue:
    def __init__(self) -> None:
        self._queue: deque[dict] = deque()

    def enqueue(self, payload: dict) -> None:
        self._queue.append(payload)

    def dequeue(self) -> dict | None:
        return self._queue.popleft() if self._queue else None

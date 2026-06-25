import logging
from pathlib import Path
from queue import PriorityQueue
from threading import Lock
from typing import List

try:
    from .task import Task
    from .worker import Worker
except ImportError:  # pragma: no cover - supports direct script execution
    from task import Task
    from worker import Worker


class Scheduler:
    def __init__(self, num_workers: int = 2, sleep_time: float = 1.0) -> None:
        self.task_queue: PriorityQueue = PriorityQueue()
        self.num_workers = num_workers
        self.sleep_time = sleep_time
        self.workers: List[Worker] = []
        self.completed_tasks = 0
        self._completed_tasks_lock = Lock()
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        logger = logging.getLogger("scheduler")
        logger.setLevel(logging.INFO)
        logger.propagate = False

        if not logger.handlers:
            log_path = Path(__file__).resolve().parent.parent / "scheduler.log"
            file_handler = logging.FileHandler(log_path)
            file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            logger.addHandler(file_handler)

        return logger

    def add_task(self, task: Task) -> None:
        priority_value = self._priority_value(task.priority)
        self.task_queue.put((priority_value, task.created_at, task))

    def _priority_value(self, priority: str) -> int:
        return {Task.HIGH: 0, Task.MEDIUM: 1, Task.LOW: 2}.get(priority, 1)

    def increment_completed_tasks(self) -> None:
        with self._completed_tasks_lock:
            self.completed_tasks += 1

    def start_workers(self) -> None:
        if self.workers:
            return

        for index in range(self.num_workers):
            worker = Worker(
                self.task_queue,
                scheduler=self,
                name=f"Worker-{index + 1}",
                sleep_time=self.sleep_time,
            )
            worker.start()
            self.workers.append(worker)

    def stop_workers(self) -> None:
        if not self.workers:
            return

        self.task_queue.join()
        for _ in self.workers:
            self.task_queue.put((999, None, None))

        for worker in self.workers:
            worker.join()

        self.workers = []

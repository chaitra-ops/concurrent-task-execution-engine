import time
from queue import PriorityQueue
from threading import Thread

try:
    from .task import Task
except ImportError:  # pragma: no cover - supports direct script execution
    from task import Task


class Worker(Thread):
    def __init__(
        self,
        task_queue: PriorityQueue,
        scheduler=None,
        name: str = "Worker",
        sleep_time: float = 1.0,
    ) -> None:
        super().__init__(name=name, daemon=True)
        self.task_queue = task_queue
        self.scheduler = scheduler
        self.sleep_time = sleep_time

    def run(self) -> None:
        while True:
            _, _, task = self.task_queue.get()
            if task is None:
                self.task_queue.task_done()
                break

            print(f"[{self.name}] received task {task.id}: {task.name}")
            try:
                task.status = Task.RUNNING
                if self.scheduler is not None:
                    self.scheduler.logger.info("task start | worker=%s | task_id=%s | task_name=%s", self.name, task.id, task.name)
                print(f"[{self.name}] running task {task.id}")
                time.sleep(self.sleep_time)
                task.status = Task.COMPLETED
                if self.scheduler is not None:
                    self.scheduler.increment_completed_tasks()
                    self.scheduler.logger.info("task completion | worker=%s | task_id=%s | task_name=%s", self.name, task.id, task.name)
                print(f"[{self.name}] completed task {task.id}")
            except Exception as exc:
                task.status = Task.FAILED
                if self.scheduler is not None:
                    self.scheduler.logger.exception("task failure | worker=%s | task_id=%s | task_name=%s | error=%s", self.name, task.id, task.name, exc)
                print(f"[{self.name}] failed task {task.id}: {exc}")
            finally:
                self.task_queue.task_done()

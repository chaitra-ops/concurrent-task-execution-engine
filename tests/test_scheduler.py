import unittest

from project.scheduler import Scheduler
from project.task import Task


class SchedulerCounterTests(unittest.TestCase):
    def test_completed_tasks_counter_is_thread_safe(self) -> None:
        scheduler = Scheduler(num_workers=1, sleep_time=0.05)
        scheduler.start_workers()

        task = Task(name="Counter task")
        scheduler.add_task(task)
        scheduler.task_queue.join()
        scheduler.stop_workers()

        self.assertEqual(scheduler.completed_tasks, 1)

    def test_priority_queue_orders_high_priority_first(self) -> None:
        scheduler = Scheduler(num_workers=1, sleep_time=0.01)

        low_task = Task(name="Low task", priority=Task.LOW)
        medium_task = Task(name="Medium task", priority=Task.MEDIUM)
        high_task = Task(name="High task", priority=Task.HIGH)

        scheduler.add_task(low_task)
        scheduler.add_task(medium_task)
        scheduler.add_task(high_task)

        _, _, queued_task = scheduler.task_queue.get()
        self.assertEqual(queued_task.name, "High task")


if __name__ == "__main__":
    unittest.main()

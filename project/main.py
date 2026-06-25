from scheduler import Scheduler
from task import Task


def main() -> None:
    scheduler = Scheduler(num_workers=2, sleep_time=0.3)
    scheduler.start_workers()

    tasks = [
        Task(name="Low task 1", priority=Task.LOW),
        Task(name="High task 1", priority=Task.HIGH),
        Task(name="Medium task 1", priority=Task.MEDIUM),
        Task(name="Low task 2", priority=Task.LOW),
        Task(name="High task 2", priority=Task.HIGH),
    ]
    for task in tasks:
        scheduler.add_task(task)

    scheduler.task_queue.join()
    scheduler.stop_workers()

    print("Priority demo completed")


if __name__ == "__main__":
    main()

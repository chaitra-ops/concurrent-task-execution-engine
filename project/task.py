from datetime import datetime, timezone
from typing import Optional
import uuid


class Task:
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(
        self,
        name: str,
        status: str = PENDING,
        created_at: Optional[datetime] = None,
        task_id: Optional[uuid.UUID] = None,
        priority: str = MEDIUM,
    ) -> None:
        self.id = str(task_id or uuid.uuid4())
        self.name = name
        self.status = status
        self.created_at = created_at or datetime.now(timezone.utc)
        self.priority = priority

    def __str__(self) -> str:
        return (
            f"Task(id={self.id}, name={self.name}, status={self.status}, "
            f"priority={self.priority}, created_at={self.created_at.isoformat()})"
        )

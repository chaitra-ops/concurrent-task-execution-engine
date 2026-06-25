# Concurrent Task Execution Engine

A Python-based multi-threaded task scheduling system that executes jobs concurrently using worker threads and priority-based scheduling.

## Overview

Modern software systems such as Gmail, YouTube, Uber, and cloud platforms process thousands of background jobs simultaneously. This project simulates how these systems manage and execute tasks efficiently using concurrency and multithreading.

The scheduler distributes tasks across worker threads, prioritizes important jobs, tracks task completion safely using synchronization mechanisms, and logs execution details for monitoring and debugging.

---

## Features

- Multi-threaded task execution
- Priority-based scheduling (HIGH, MEDIUM, LOW)
- Thread-safe task processing
- Synchronization using Locks
- Completed-task tracking
- Structured logging
- Automated unit testing
- Modular software architecture

---

## Concepts Demonstrated

### Software Engineering

- Modular Design
- Separation of Concerns
- Testing
- Logging

### Concurrency

- Concurrent Task Processing
- Worker Thread Pool
- Thread-Safe Queues

### Synchronization

- Race Condition Prevention
- Lock-Based Synchronization
- Shared Resource Protection

### Data Structures

- Queue
- Priority Queue

---

## Architecture

```text
                Scheduler
                     │
                     ▼
             Priority Queue
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
  Worker-1      Worker-2      Worker-3
      │              │              │
      ▼              ▼              ▼
 Execute Task   Execute Task   Execute Task
      │              │              │
      └──────────┬───┴──────────────┘
                 ▼
          Lock Protected
          Completion Counter
                 │
                 ▼
               Logging
```

## Project Structure

```text
project/
├── task.py
├── worker.py
├── scheduler.py
├── main.py
├── tests/
│   └── test_scheduler.py
└── scheduler.log
```

## Technologies Used

- Python 3
- threading
- queue.PriorityQueue
- logging
- unittest

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/concurrent-task-execution-engine.git
cd concurrent-task-execution-engine
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Run the scheduler:

```bash
python3 project/main.py
```

Run tests:

```bash
python3 -m unittest tests.test_scheduler
```

---

## Example Output

```text
[Worker-1] running task: High Priority Task
[Worker-2] running task: Medium Priority Task
[Worker-3] running task: Low Priority Task

All tasks completed
```

---

## Key Learnings

Through this project I gained practical experience with:

- Concurrency
- Multithreading
- Synchronization
- Thread Safety
- Priority Scheduling
- Logging
- Unit Testing
- Software Design Principles

---

## Future Improvements

- Retry mechanism for failed tasks
- FastAPI integration
- Real-time monitoring dashboard
- Task persistence using a database
- Distributed worker support

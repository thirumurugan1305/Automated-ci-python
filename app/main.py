"""
Task Manager API
-----------------
A simple FastAPI application that manages tasks using an in-memory
data structure. Built to demonstrate a Continuous Integration workflow
with GitHub Actions, not as a production-grade service.
"""

from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task Manager API", version="1.0.0")


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

class TaskCreate(BaseModel):
    """Fields required to create a new task."""

    title: str = Field(..., min_length=1, description="Short title of the task")
    description: str = Field(default="", description="Optional task details")


class TaskUpdate(BaseModel):
    """Fields allowed when updating an existing task. All optional."""

    title: Optional[str] = Field(default=None, min_length=1)
    description: Optional[str] = None
    completed: Optional[bool] = None


class Task(BaseModel):
    """Full representation of a task returned to clients."""

    id: int
    title: str
    description: str
    completed: bool = False


# ---------------------------------------------------------------------------
# In-memory storage
# ---------------------------------------------------------------------------

# tasks_db maps task id -> Task. next_id tracks the next id to assign.
tasks_db: dict[int, Task] = {}
next_id: int = 1


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/", status_code=status.HTTP_200_OK)
def health_check() -> dict:
    """Basic health/status endpoint used to confirm the app is running."""
    return {"status": "ok", "message": "Task Manager API is running"}


@app.get("/tasks", status_code=status.HTTP_200_OK)
def get_tasks() -> list[Task]:
    """Return all tasks currently stored in memory."""
    return list(tasks_db.values())


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate) -> Task:
    """Create a new task and store it in memory."""
    global next_id

    new_task = Task(
        id=next_id,
        title=task_in.title,
        description=task_in.description,
        completed=False,
    )
    tasks_db[next_id] = new_task
    next_id += 1
    return new_task


@app.get("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def get_task(task_id: int) -> Task:
    """Retrieve a single task by id, or 404 if it does not exist."""
    task = tasks_db.get(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, task_in: TaskUpdate) -> Task:
    """Update an existing task. Only provided fields are changed."""
    existing_task = tasks_db.get(task_id)
    if existing_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    updated_data = existing_task.model_copy(
        update={
            key: value
            for key, value in task_in.model_dump(exclude_unset=True).items()
        }
    )
    tasks_db[task_id] = updated_data
    return updated_data


@app.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int) -> dict:
    """Delete a task by id, or 404 if it does not exist."""
    if task_id not in tasks_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

    del tasks_db[task_id]
    return {"message": f"Task {task_id} deleted successfully"}

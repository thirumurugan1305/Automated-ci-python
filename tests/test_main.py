"""
Automated test suite for the Task Manager API.

These tests use FastAPI's TestClient to send real HTTP-style requests
to the application and verify actual response behavior (status codes
and JSON payloads), not just that files or functions exist.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app, tasks_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_tasks_db():
    """Ensure each test starts with a clean, empty task store."""
    tasks_db.clear()
    yield
    tasks_db.clear()


def test_health_check():
    """GET / should report that the application is running."""
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"


def test_create_task():
    """POST /tasks should create a task and return it with an id."""
    payload = {"title": "Write report", "description": "Q3 summary"}
    response = client.post("/tasks", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "Write report"
    assert body["description"] == "Q3 summary"
    assert body["completed"] is False
    assert "id" in body


def test_get_all_tasks():
    """GET /tasks should return every task that has been created."""
    client.post("/tasks", json={"title": "Task A"})
    client.post("/tasks", json={"title": "Task B"})

    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 2
    titles = {task["title"] for task in tasks}
    assert titles == {"Task A", "Task B"}


def test_get_single_task():
    """GET /tasks/{id} should return the specific task requested."""
    create_response = client.post("/tasks", json={"title": "Buy groceries"})
    task_id = create_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Buy groceries"


def test_update_task():
    """PUT /tasks/{id} should update only the provided fields."""
    create_response = client.post("/tasks", json={"title": "Old title"})
    task_id = create_response.json()["id"]

    response = client.put(f"/tasks/{task_id}", json={"title": "New title", "completed": True})
    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "New title"
    assert body["completed"] is True


def test_delete_task():
    """DELETE /tasks/{id} should remove the task from storage."""
    create_response = client.post("/tasks", json={"title": "Temporary task"})
    task_id = create_response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200

    # The task should no longer be retrievable.
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


def test_get_nonexistent_task_returns_404():
    """GET on a task id that was never created should return 404."""
    response = client.get("/tasks/9999")
    assert response.status_code == 404


def test_update_nonexistent_task_returns_404():
    """PUT on a task id that does not exist should return 404."""
    response = client.put("/tasks/9999", json={"title": "Does not matter"})
    assert response.status_code == 404


def test_delete_nonexistent_task_returns_404():
    """DELETE on a task id that does not exist should return 404."""
    response = client.delete("/tasks/9999")
    assert response.status_code == 404


def test_create_task_with_invalid_data_returns_422():
    """POST /tasks with an empty title should fail validation."""
    response = client.post("/tasks", json={"title": ""})
    assert response.status_code == 422


def test_create_task_missing_title_returns_422():
    """POST /tasks without a title field at all should fail validation."""
    response = client.post("/tasks", json={"description": "No title provided"})
    assert response.status_code == 422

# Automated CI Pipeline for Python Task Manager

## 1. Project Overview

This project is a small **Task Manager API** built with FastAPI, paired with an automated Pytest test suite and a **GitHub Actions** Continuous Integration (CI) workflow.

- **What the application does:** it lets a client create, read, update, and delete simple in-memory tasks over HTTP.
- **What CI means in this project:** every time code is pushed to GitHub (or a pull request is opened/updated), an automated pipeline installs the project's dependencies and runs the full test suite, so bugs are caught immediately instead of being discovered later.
- **Why GitHub Actions:** it is GitHub's native automation platform, requires no external CI server, and is triggered directly by repository events (push/PR), making it a natural fit for demonstrating CI end-to-end.

The application itself is intentionally simple — the point of this project is the **pipeline**, not the API.

## 2. Architecture / Workflow

```text
Code Change
    ↓
GitHub Push / Pull Request
    ↓
GitHub Actions
    ↓
Install Dependencies
    ↓
Run Pytest
    ↓
Pass / Fail
```

## 3. Features

- Health/status check endpoint
- Create a task
- Retrieve all tasks
- Retrieve a single task by id
- Update an existing task (partial updates supported)
- Delete a task
- Proper HTTP status codes and error handling (404 for missing tasks, 422 for invalid input)

## 4. Technologies Used

- Python 3
- FastAPI
- Pytest
- GitHub Actions
- Git / GitHub

## 5. Project Structure

```text
automated-ci-python/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_main.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── .gitignore
├── README.md
├── INTERVIEW_NOTES.md
└── LICENSE
```

## 6. Local Setup

### Clone the repository

```bash
git clone <your-repository-url>
cd automated-ci-python
```

### Create and activate a virtual environment

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive docs are available at `http://127.0.0.1:8000/docs`.

### Run tests

```bash
pytest -v
```

## 7. API Endpoints

| Method | Endpoint    | Purpose      |
| ------ | ----------- | ------------ |
| GET    | /           | Health check |
| GET    | /tasks      | Get tasks    |
| POST   | /tasks      | Create task  |
| GET    | /tasks/{id} | Get task     |
| PUT    | /tasks/{id} | Update task  |
| DELETE | /tasks/{id} | Delete task  |

## 8. CI Pipeline

When code is pushed to GitHub (or a pull request is created/updated), the workflow defined in `.github/workflows/ci.yml` runs automatically:

1. The repository is checked out onto a GitHub-hosted runner.
2. Python 3.11 is installed on the runner.
3. Dependencies are installed from `requirements.txt`.
4. `pytest -v` is executed against the full test suite.
5. If every test passes, the workflow reports **success** (green check). If any test fails, the workflow reports **failure** (red X) and stops the pipeline there — there is no later stage in this project.

## 9. Testing

The test suite in `tests/test_main.py` uses FastAPI's `TestClient` (built on `httpx`) to send real HTTP requests to the application in-process and assert on the actual responses. It covers:

- The health check endpoint
- Creating a task
- Listing all tasks
- Retrieving a single task
- Updating a task
- Deleting a task
- 404 handling for a task id that doesn't exist (get, update, delete)
- 422 handling for invalid input (empty title, missing title)

Each test resets the in-memory task store beforehand via an autouse fixture, so tests do not interfere with each other.

## 10. Future Improvements

These are realistic next steps for later projects and are **not** implemented here:

- Docker containerization
- Continuous Deployment (CD) to a hosting platform
- Cloud deployment (AWS/Azure/GCP)
- Monitoring and alerting (e.g., Prometheus/Grafana)
- Infrastructure as Code (e.g., Terraform)

## 11. License

This project is licensed under the [MIT License](./LICENSE).

---

## RESUME DESCRIPTION

### Project Title

Automated CI Pipeline for a Python Task Manager API

### One-line Description

Built a FastAPI Task Manager API with an automated Pytest test suite and a GitHub Actions CI pipeline that runs tests on every push and pull request.

### Resume Bullet Points

- Developed a RESTful Task Manager API in Python using FastAPI, implementing CRUD endpoints with input validation and proper HTTP status code handling.
- Wrote an automated test suite with Pytest and FastAPI's TestClient, covering core functionality, edge cases, and error handling (404/422 responses).
- Configured a GitHub Actions CI workflow to automatically install dependencies and run the test suite on every push and pull request, ensuring code changes are validated before merging.

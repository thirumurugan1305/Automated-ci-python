# Automated CI Pipeline for Python Task Manager

## 1. Project Overview

This project is a small **Task Manager API** built with FastAPI, paired with an automated Pytest test suite and a **GitHub Actions Continuous Integration (CI)** workflow.

### What the application does

It allows a client to create, read, update, and delete simple in-memory tasks over HTTP.

### What CI means in this project

Every time code is pushed to GitHub, or a pull request is opened or updated, an automated pipeline installs the project's dependencies and runs the full test suite.

This helps detect bugs automatically whenever code changes are made.

### Why GitHub Actions?

GitHub Actions is GitHub's native automation platform. It allows the CI process to run automatically without requiring a separate CI server.

The application itself is intentionally simple. The main purpose of this project is to demonstrate the **Continuous Integration pipeline**.

---

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

---

## 3. Features

* Health/status check endpoint
* Create a task
* Retrieve all tasks
* Retrieve a single task by ID
* Update an existing task
* Delete a task
* Input validation
* Proper HTTP status codes
* 404 handling for missing tasks
* 422 handling for invalid input
* Automated testing using Pytest
* Automated CI using GitHub Actions

---

## 4. Technologies Used

* **Python 3**
* **FastAPI**
* **Pytest**
* **GitHub Actions**
* **Git**
* **GitHub**

---

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

---

## 6. Local Setup

### Clone the repository

```bash
git clone <your-repository-url>
cd automated-ci-python
```

### Create and activate a virtual environment

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### Run tests

```bash
pytest -v
```

---

## 7. API Endpoints

| Method | Endpoint      | Purpose             |
| ------ | ------------- | ------------------- |
| GET    | `/`           | Health check        |
| GET    | `/tasks`      | Get all tasks       |
| POST   | `/tasks`      | Create a task       |
| GET    | `/tasks/{id}` | Get a specific task |
| PUT    | `/tasks/{id}` | Update a task       |
| DELETE | `/tasks/{id}` | Delete a task       |

---

## 8. CI Pipeline

When code is pushed to GitHub, or a pull request is created or updated, the workflow defined in `.github/workflows/ci.yml` runs automatically.

The pipeline performs the following steps:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs dependencies from `requirements.txt`.
4. Runs the Pytest test suite.
5. Reports whether the tests passed or failed.

If the tests pass, GitHub Actions reports a successful workflow.

If any test fails, the workflow fails.

```text
Git Push / Pull Request
          ↓
    GitHub Actions
          ↓
    Checkout Code
          ↓
     Setup Python
          ↓
 Install Dependencies
          ↓
       Run Pytest
          ↓
     ┌────┴────┐
     ↓         ↓
   PASS       FAIL
   Green       Red
```

---

## 9. Testing

The test suite is located in:

```text
tests/test_main.py
```

It uses **Pytest** and FastAPI's **TestClient** to test the actual API behavior.

The test suite covers:

* Health check
* Creating a task
* Listing all tasks
* Retrieving a single task
* Updating a task
* Deleting a task
* Handling a non-existing task
* Handling invalid input
* Handling missing required fields

### Test Result

The complete test suite was executed locally:

```text
11 passed
```

The tests were successfully executed using:

```bash
pytest -v
```

---

## 10. Future Improvements

The following are possible improvements for future DevOps projects and are **not implemented in this project**:

* Docker containerization
* Continuous Deployment (CD)
* Cloud deployment
* AWS / Azure / Google Cloud
* Monitoring and alerting
* Prometheus and Grafana
* Infrastructure as Code using Terraform
* Database integration

---

## 11. License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

# Resume Description

## Project Title

**Automated CI Pipeline for a Python Task Manager API**

## One-line Description

Built a FastAPI Task Manager API with an automated Pytest test suite and a GitHub Actions CI pipeline that runs tests on every push and pull request.

## Resume Bullet Points

* Developed a RESTful Task Manager API in Python using FastAPI, implementing CRUD operations with input validation and appropriate HTTP status codes.
* Created an automated test suite using Pytest and FastAPI TestClient, covering core functionality, edge cases, and error handling.
* Configured a GitHub Actions CI workflow to automatically install dependencies and execute the test suite on every push and pull request.
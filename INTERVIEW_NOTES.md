# Interview Notes

Beginner-friendly explanations of the concepts demonstrated by this project.

## 1. What is DevOps?

DevOps is a set of practices that combines software **development** and IT **operations**, aiming to shorten the development lifecycle and deliver reliable software faster through automation, collaboration, and continuous feedback.

## 2. What is Continuous Integration?

Continuous Integration (CI) is the practice of automatically building and testing code every time a change is pushed to a shared repository. It helps catch bugs early, before they reach production.

## 3. What is GitHub Actions?

GitHub Actions is GitHub's built-in automation platform. It lets you define workflows — sequences of automated steps — that run in response to repository events like a push or a pull request.

## 4. What is a workflow?

A workflow is a YAML file (stored in `.github/workflows/`) that defines when automation should run (the trigger) and what steps it should perform (checkout code, install dependencies, run tests, etc.).

## 5. What is a GitHub Actions runner?

A runner is the machine (virtual environment) that actually executes the steps in a workflow. GitHub provides hosted runners (e.g., `ubuntu-latest`) so you don't need your own infrastructure.

## 6. What is Pytest?

Pytest is a popular Python testing framework used to write and run automated tests. It supports simple `assert` statements, fixtures for setup/teardown, and clear, readable test output.

## 7. Why are automated tests important?

Automated tests verify that the application behaves as expected, without requiring a person to manually check every feature after every change. They catch regressions early and give developers confidence to change code safely.

## 8. What happens when code is pushed to GitHub?

If a GitHub Actions workflow is configured to trigger `on: push`, GitHub automatically starts a new workflow run: it spins up a runner, checks out the code, and executes the defined steps (like installing dependencies and running tests).

## 9. What happens when a test fails?

If any test in the suite fails, the test command (`pytest`) exits with a non-zero status code. GitHub Actions detects this and marks the workflow run as **failed**, which is visible directly in the GitHub repository (a red X instead of a green check).

## 10. Why use a virtual environment?

A virtual environment isolates a project's Python dependencies from the system Python installation and from other projects, preventing version conflicts and keeping dependencies reproducible.

## 11. What is FastAPI?

FastAPI is a modern, high-performance Python web framework for building APIs. It uses Python type hints to provide automatic request validation, serialization, and interactive API documentation.

## 12. What is an API?

An API (Application Programming Interface) is a defined way for one piece of software to communicate with another — in this project, clients send HTTP requests (GET, POST, PUT, DELETE) to interact with the Task Manager.

## 13. What is the difference between CI and CD?

- **CI (Continuous Integration):** automatically building and testing code changes.
- **CD (Continuous Delivery/Deployment):** automatically releasing tested code to a staging or production environment.

This project implements CI only — it does not deploy the application anywhere.

## 14. Why is this project considered a DevOps project?

It demonstrates a core DevOps practice — automating the testing feedback loop between writing code and validating it — using real tools (Git, GitHub, GitHub Actions, Pytest) rather than manual, ad-hoc testing.

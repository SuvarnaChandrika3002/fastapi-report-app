FastAPI Report & History Web Application

A full-stack FastAPI application featuring calculation operations, history tracking, reporting statistics, automated testing (unit, integration, E2E), Docker containerization, and CI/CD deployment through GitHub Actions.

Features
Calculator

Supports operations: +, -, *, /, ^ (exponentiation)

Front-end form performs calculations via /api/calculate

Calculation History

Stores every calculation in the database

/api/history returns the latest 20 calculations

History table visible on the UI

Report / Statistics

Generated from all stored calculations:

Total number of calculations

Sum of results

Average result

Count per operation

Displayed live on the front-end

Fully Tested

Unit tests → pure calculation logic

Integration tests → API + DB

Playwright E2E tests → full user workflow in the browser

All tests run automatically via GitHub Actions

Docker Support

Fully containerized

CI pipeline builds and pushes to Docker Hub

Publicly available image

Installation & Setup
Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows

Running the Application Locally

Start FastAPI server:

uvicorn app.main:app --reload


Open in your browser:

http://127.0.0.1:8000

Running Tests
Unit & Integration Tests
pytest
Playwright E2E Tests
Terminal 1:
uvicorn app.main:app --host 127.0.0.1 --port 8000
Terminal 2:
npx playwright test
Docker Usage
Build the Docker image:
docker build -t sc673/finalprojet:latest .

Run the Docker container:
docker run -p 8000:8000 sc673/finalprojet:latest
Visit:
http://localhost:8000
CI/CD Pipeline (GitHub Actions)

Your CI workflow performs:

Install Python dependencies

Run pytest (unit + integration)

Install Playwright + browsers

Start FastAPI for E2E

Run Playwright tests

Build Docker image

Push to Docker Hub automatically

Workflow file:
.github/workflows/ci.yml

Docker Hub Repository

Image automatically published to Docker Hub:

🔗 https://hub.docker.com/r/sc673/finalprojet

You can pull it using:

docker pull sc673/finalprojet:latest

📎 GitHub Repository Link

🔗 https://github.com/SuvarnaChandrika3002/fastapi-report-app

Summary

This project demonstrates:

Full FastAPI backend with SQLAlchemy

Templated front-end UI

Persistent calculation storage

History + advanced report metrics

Unit, integration, and E2E tests

Fully automated CI/CD pipeline

Docker containerization & deployment

It is a complete, production-ready example of a small but fully tested web application
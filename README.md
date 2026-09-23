# API Integration Service

[![Live Demo](https://img.shields.io/badge/Live_Demo-Open_App-4C6EF5?style=for-the-badge)](https://api-integration-service.onrender.com/)
[![API Docs](https://img.shields.io/badge/API_Docs-Swagger-009688?style=for-the-badge)](https://api-integration-service.onrender.com/docs)
[![GitHub](https://img.shields.io/badge/Source_Code-GitHub-181717?style=for-the-badge&logo=github)](https://github.com/Veropa123/api-integration-service)

A production-style backend project for consuming, validating, normalizing, persisting, and exposing third-party API data.

> **Live application:** https://api-integration-service.onrender.com/

## Overview

This project demonstrates a common real-world backend workflow:

```text
External REST API
       |
       v
HTTPX integration client
       |
       v
Pydantic validation / normalization
       |
       v
FastAPI application
       |
       +----> REST endpoints
       |
       +----> SQLAlchemy persistence
       |
       +----> Interactive dashboard
```

The demo integrates with the public JSONPlaceholder users API. The provider-specific logic is isolated in its own integration client so another upstream API can be introduced without rewriting the persistence or API layers.

## Features

- External REST API integration with HTTPX
- Third-party payload normalization
- Typed request/response models
- FastAPI REST endpoints
- Upstream failure handling with HTTP 502 responses
- Structured application logging
- SQLAlchemy persistence
- SQLite local development
- PostgreSQL-ready configuration through `DATABASE_URL`
- Synchronization workflow with insert/update logic
- Lightweight browser dashboard
- Swagger/OpenAPI documentation
- Pytest automated tests
- Docker and Docker Compose
- GitHub Actions continuous integration
- Public deployment on Render

## Tech Stack

- Python
- FastAPI
- HTTPX
- Pydantic / Pydantic Settings
- SQLAlchemy
- SQLite / PostgreSQL
- JavaScript
- HTML/CSS
- Pytest
- Docker
- GitHub Actions
- Render

## API Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/` | Browser dashboard |
| GET | `/health` | Application health check |
| GET | `/external/users` | Fetch and normalize users directly from the upstream provider |
| POST | `/sync/users` | Synchronize upstream users into the local database |
| GET | `/users` | Return persisted synchronized users |
| GET | `/docs` | Interactive Swagger/OpenAPI documentation |

## Live Demo

Open the deployed application:

https://api-integration-service.onrender.com/

Interactive API documentation:

https://api-integration-service.onrender.com/docs

Health check:

https://api-integration-service.onrender.com/health

> The free Render instance may take a short time to wake up after periods of inactivity.

## Project Structure

```text
api-integration-service/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── integrations/
│   │   └── jsonplaceholder.py
│   ├── services/
│   │   └── sync_service.py
│   ├── static/
│   │   └── index.html
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── tests/
│   ├── test_external_client.py
│   └── test_health.py
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├── pytest.ini
├── README.md
├── render.yaml
└── requirements.txt
```

## Run Locally

```bash
git clone https://github.com/Veropa123/api-integration-service.git
cd api-integration-service
python -m venv .venv
```

Activate on Windows:

```bash
.venv\Scripts\activate
```

Activate on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies and start the app:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open:

```text
Dashboard: http://127.0.0.1:8000
API docs:  http://127.0.0.1:8000/docs
```

## Docker

```bash
docker compose up --build
```

## Testing

```bash
pytest
```

GitHub Actions runs the test suite automatically on pushes to `main` and on pull requests.

## Environment Variables

```env
APP_NAME=API Integration Service
APP_ENV=development
DATABASE_URL=sqlite:///./integration.db
UPSTREAM_BASE_URL=https://jsonplaceholder.typicode.com
REQUEST_TIMEOUT_SECONDS=10
```

For PostgreSQL, replace `DATABASE_URL` with a SQLAlchemy-compatible PostgreSQL connection string.

## Demo Workflow

1. Open the dashboard.
2. Click **Sync external API**.
3. The application fetches data from the third-party API.
4. The integration client normalizes the provider-specific payload.
5. The sync service inserts new records or updates existing records.
6. The dashboard loads the synchronized users from the application's API.
7. Swagger documentation can be used to inspect and test every endpoint directly.

## Portfolio Purpose

This project is designed as a complete backend case study rather than a simple API-call example. It demonstrates separation of concerns, integration boundaries, typed models, persistence, error handling, testing, containerization, CI, deployment, and technical documentation.

## Status

**Live and publicly deployed.**

## License

MIT

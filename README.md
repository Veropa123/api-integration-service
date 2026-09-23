# API Integration Service

A production-style REST API integration project built with Python and FastAPI.

This service demonstrates how to consume an external API, validate and normalize third-party data, persist synchronized records, expose documented endpoints, handle upstream failures, and package the application for deployment.

## Project Goals

- Integrate safely with an external REST API
- Normalize third-party data into typed application models
- Persist synchronized records with SQLAlchemy
- Support SQLite locally and PostgreSQL through `DATABASE_URL`
- Provide clear error handling and logging
- Expose interactive OpenAPI documentation
- Include automated tests, Docker, CI, and deployment configuration

## Current Status

**In development**

The first implementation includes the external client, API endpoints, persistence layer, a lightweight dashboard, automated tests, Docker, and CI.

## Tech Stack

- Python
- FastAPI
- HTTPX
- Pydantic
- SQLAlchemy
- SQLite / PostgreSQL-ready
- JavaScript
- Pytest
- Docker
- GitHub Actions

## External API

The demo integrates with JSONPlaceholder's public users API. The integration layer is isolated so the upstream provider can be replaced without changing the API routes or persistence logic.

## Planned Deployment

Render web service using the included Dockerfile and `render.yaml`.

## License

MIT

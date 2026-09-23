import logging
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.config import settings
from app.database import Base, engine, get_db
from app.integrations.jsonplaceholder import UpstreamAPIError
from app.schemas import HealthResponse, SyncResult, SyncedUserResponse
from app.services.sync_service import list_synced_users, sync_users

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

BASE_DIR = Path(__file__).resolve().parent

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Production-style service for synchronizing and exposing third-party API data.",
)


@app.get("/", include_in_schema=False)
def dashboard() -> FileResponse:
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", environment=settings.app_env)


@app.get("/external/users", response_model=list[SyncedUserResponse])
async def external_users() -> list[SyncedUserResponse]:
    from app.integrations.jsonplaceholder import JsonPlaceholderClient

    client = JsonPlaceholderClient()

    try:
        users = await client.fetch_users()
    except UpstreamAPIError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    return [SyncedUserResponse(**user.model_dump()) for user in users]


@app.post("/sync/users", response_model=SyncResult)
async def synchronize_users(
    db: Session = Depends(get_db),
) -> SyncResult:
    try:
        return await sync_users(db)
    except UpstreamAPIError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/users", response_model=list[SyncedUserResponse])
def users(db: Session = Depends(get_db)) -> list[SyncedUserResponse]:
    return list_synced_users(db)

import logging

import httpx

from app.config import settings
from app.schemas import ExternalUser

logger = logging.getLogger(__name__)


class UpstreamAPIError(RuntimeError):
    pass


class JsonPlaceholderClient:
    def __init__(self) -> None:
        self.base_url = settings.upstream_base_url.rstrip("/")
        self.timeout = settings.request_timeout_seconds

    async def fetch_users(self) -> list[ExternalUser]:
        url = f"{self.base_url}/users"

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url)
                response.raise_for_status()
                payload = response.json()
        except (httpx.HTTPError, ValueError) as exc:
            logger.exception("Failed to fetch users from upstream API")
            raise UpstreamAPIError("Upstream user service is unavailable.") from exc

        users: list[ExternalUser] = []
        for item in payload:
            users.append(
                ExternalUser(
                    id=item["id"],
                    name=item["name"],
                    username=item["username"],
                    email=item["email"],
                    phone=item["phone"],
                    website=item["website"],
                    company=item.get("company", {}).get("name", "Unknown"),
                    city=item.get("address", {}).get("city", "Unknown"),
                )
            )

        return users

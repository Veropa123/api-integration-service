from sqlalchemy import select
from sqlalchemy.orm import Session

from app.integrations.jsonplaceholder import JsonPlaceholderClient
from app.models import SyncedUser
from app.schemas import ExternalUser, SyncResult


async def sync_users(db: Session) -> SyncResult:
    client = JsonPlaceholderClient()
    upstream_users = await client.fetch_users()

    imported = 0
    updated = 0

    for user in upstream_users:
        existing = db.get(SyncedUser, user.id)

        if existing is None:
            db.add(_to_model(user))
            imported += 1
        else:
            _update_model(existing, user)
            updated += 1

    db.commit()

    return SyncResult(
        imported=imported,
        updated=updated,
        total_upstream=len(upstream_users),
    )


def list_synced_users(db: Session) -> list[SyncedUser]:
    return list(
        db.scalars(select(SyncedUser).order_by(SyncedUser.id)).all()
    )


def _to_model(user: ExternalUser) -> SyncedUser:
    return SyncedUser(
        id=user.id,
        name=user.name,
        username=user.username,
        email=str(user.email),
        phone=user.phone,
        website=user.website,
        company=user.company,
        city=user.city,
    )


def _update_model(model: SyncedUser, user: ExternalUser) -> None:
    model.name = user.name
    model.username = user.username
    model.email = str(user.email)
    model.phone = user.phone
    model.website = user.website
    model.company = user.company
    model.city = user.city

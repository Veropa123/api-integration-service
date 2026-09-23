from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class SyncedUser(Base):
    __tablename__ = "synced_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    username: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(180), index=True)
    phone: Mapped[str] = mapped_column(String(120))
    website: Mapped[str] = mapped_column(String(180))
    company: Mapped[str] = mapped_column(String(180))
    city: Mapped[str] = mapped_column(String(120))

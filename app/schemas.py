from pydantic import BaseModel, ConfigDict, EmailStr


class ExternalUser(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    phone: str
    website: str
    company: str
    city: str


class SyncedUserResponse(ExternalUser):
    model_config = ConfigDict(from_attributes=True)


class SyncResult(BaseModel):
    imported: int
    updated: int
    total_upstream: int


class HealthResponse(BaseModel):
    status: str
    environment: str

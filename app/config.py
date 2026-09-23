from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "API Integration Service"
    app_env: str = "development"
    database_url: str = "sqlite:///./integration.db"
    upstream_base_url: str = "https://jsonplaceholder.typicode.com"
    request_timeout_seconds: float = 10.0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()

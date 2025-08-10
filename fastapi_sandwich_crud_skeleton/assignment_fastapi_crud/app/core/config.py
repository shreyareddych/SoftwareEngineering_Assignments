"""Application configuration (dotenv optional) - Skeleton."""
from pydantic import BaseModel
import os

class Settings(BaseModel):
    APP_NAME: str = "Sandwich Maker CRUD API"
    ENV: str = os.getenv("ENV", "dev")
    # Use SQLite by default for student convenience; replace with Postgres if needed
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL", "sqlite:///./sandwich.db")  # TODO: change if needed

def get_settings() -> Settings:
    # Could cache with lru_cache if desired
    return Settings()

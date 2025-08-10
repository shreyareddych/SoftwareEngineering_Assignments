"""DB engine and session factory - Skeleton."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
from app.core.config import get_settings

settings = get_settings()

# SQLite: need check_same_thread=False for typical FastAPI demo
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False} if settings.SQLALCHEMY_DATABASE_URI.startswith("sqlite") else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db() -> None:
    """Create tables if not using Alembic migrations."""
    # TODO: Use Alembic instead for real projects. For assignment, Base.metadata.create_all is fine.
    Base.metadata.create_all(bind=engine)

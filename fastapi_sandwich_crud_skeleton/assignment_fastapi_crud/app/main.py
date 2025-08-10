"""FastAPI app entrypoint - Skeleton (no README, conventional commits encouraged)."""
from fastapi import FastAPI
from app.api.routes.sandwiches import router as sandwiches_router
from app.db.session import init_db

app = FastAPI(title="Sandwich Maker CRUD API")  # TODO: add version/metadata as needed

# Include routers
app.include_router(sandwiches_router)

# Initialize DB on startup (only for simple assignment use; prefer Alembic migrations otherwise)
@app.on_event("startup")
def on_startup() -> None:
    init_db()

# Healthcheck
@app.get("/healthz")
def healthz():
    return {"status": "ok"}

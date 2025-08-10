from fastapi import FastAPI
from app.db.session import Base, engine
from app.models.model_loader import import_models

app = FastAPI(title="Online Restaurant Ordering System", version="0.1.0")

@app.on_event("startup")
def on_startup() -> None:
    import_models()
    Base.metadata.create_all(bind=engine)

@app.get("/", tags=["root"])
def root():
    return {"message": "API running"}

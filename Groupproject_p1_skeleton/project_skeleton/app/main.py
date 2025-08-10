from fastapi import FastAPI
# TODO: from app.api.v1.endpoints import users, restaurants, orders

app = FastAPI(title="Project Skeleton", version="0.1.0")

@app.get("/", tags=["root"])
def root():
    return {"message": "skeleton running"}  # keep a trivial health for CI

# TODO: app.include_router(users.router, prefix="/api/v1/users")
# TODO: app.include_router(restaurants.router, prefix="/api/v1/restaurants")
# TODO: app.include_router(orders.router, prefix="/api/v1/orders")

"""Sandwich routes - Skeleton."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app import schemas, crud, models

router = APIRouter(prefix="/sandwiches", tags=["sandwiches"])

@router.get("/", response_model=List[schemas.sandwich.SandwichOut])
def list_sandwiches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """List sandwiches with pagination."""
    # TODO: return crud.sandwich.list(db, skip, limit)
    raise NotImplementedError

@router.get("/{sandwich_id}", response_model=schemas.sandwich.SandwichOut)
def get_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    """Retrieve a sandwich by id."""
    # TODO: obj = crud.sandwich.get(...); raise 404 if None
    raise NotImplementedError

@router.post("/", response_model=schemas.sandwich.SandwichOut, status_code=status.HTTP_201_CREATED)
def create_sandwich(payload: schemas.sandwich.SandwichCreate, db: Session = Depends(get_db)):
    """Create a sandwich."""
    # TODO: check duplicate by name via crud.sandwich.get_by_name
    raise NotImplementedError

@router.patch("/{sandwich_id}", response_model=schemas.sandwich.SandwichOut)
def update_sandwich(sandwich_id: int, payload: schemas.sandwich.SandwichUpdate, db: Session = Depends(get_db)):
    """Update fields of a sandwich."""
    # TODO
    raise NotImplementedError

@router.delete("/{sandwich_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    """Delete a sandwich."""
    # TODO
    raise NotImplementedError

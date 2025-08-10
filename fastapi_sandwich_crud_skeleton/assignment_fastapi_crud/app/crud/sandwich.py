"""CRUD operations for Sandwich - Skeleton."""
from typing import List, Optional
from sqlalchemy.orm import Session
from app import models, schemas

# NOTE: Replace `pass` with working code per assignment.

def get(db: Session, sandwich_id: int) -> Optional[models.sandwich.Sandwich]:
    """Return sandwich by primary key."""
    # TODO: db.query(...).get(...) or scalar(select(...))
    pass

def get_by_name(db: Session, name: str) -> Optional[models.sandwich.Sandwich]:
    """Return sandwich by unique name."""
    # TODO
    pass

def list(db: Session, skip: int = 0, limit: int = 100) -> List[models.sandwich.Sandwich]:
    """Return paginated list of sandwiches."""
    # TODO
    pass

def create(db: Session, obj_in: schemas.sandwich.SandwichCreate) -> models.sandwich.Sandwich:
    """Create and persist a sandwich."""
    # TODO
    pass

def update(db: Session, db_obj: models.sandwich.Sandwich, obj_in: schemas.sandwich.SandwichUpdate) -> models.sandwich.Sandwich:
    """Apply partial updates and persist."""
    # TODO
    pass

def delete(db: Session, db_obj: models.sandwich.Sandwich) -> None:
    """Delete sandwich."""
    # TODO
    pass

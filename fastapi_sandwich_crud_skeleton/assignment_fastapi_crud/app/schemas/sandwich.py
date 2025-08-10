"""Pydantic schemas for Sandwich - Skeleton."""
from typing import Dict, Optional
from pydantic import BaseModel, Field, ConfigDict

class SandwichBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., ge=0.0)
    ingredients: Dict[str, float] = Field(default_factory=dict)   # amounts in grams/ml/slices
    description: Optional[str] = Field(default=None, max_length=255)

class SandwichCreate(SandwichBase):
    pass

class SandwichUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    price: Optional[float] = Field(default=None, ge=0.0)
    ingredients: Optional[Dict[str, float]] = None
    description: Optional[str] = Field(default=None, max_length=255)

class SandwichOut(SandwichBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

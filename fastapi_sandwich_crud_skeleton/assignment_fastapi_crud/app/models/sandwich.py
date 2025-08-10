"""SQLAlchemy model for Sandwich - Skeleton."""
from sqlalchemy import Column, Integer, String, Float, JSON
from app.db.base import Base

class Sandwich(Base):
    __tablename__ = "sandwiches"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)           # e.g., "small", "turkey deluxe"
    price = Column(Float, nullable=False)                              # in dollars
    ingredients = Column(JSON, nullable=False, default=dict)           # {"bread":2,"ham":50,...}
    description = Column(String(255), nullable=True)                   # optional

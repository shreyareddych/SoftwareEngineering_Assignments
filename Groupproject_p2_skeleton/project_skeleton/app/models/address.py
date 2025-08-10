from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base

class Address(Base):
    __tablename__ = "addresses"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # TODO: user_id (FK users.id), line1, line2, city, state, postal_code, country

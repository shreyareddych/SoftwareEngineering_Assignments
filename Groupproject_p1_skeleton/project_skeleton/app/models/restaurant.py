from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base

class Restaurant(Base):
    __tablename__ = "restaurants"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # TODO: name (unique), is_active

from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # TODO: user_id (FK), restaurant_id (FK), status, totals (subtotal/tax/total), delivery_address_id (FK?)

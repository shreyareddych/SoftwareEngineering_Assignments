from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base

class OrderItem(Base):
    __tablename__ = "order_items"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # TODO: order_id (FK), menu_item_id (FK), quantity, unit_price, line_total

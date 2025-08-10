from pydantic import BaseModel
from typing import List

class OrderItemIn(BaseModel):
    # TODO: menu_item_id, quantity
    pass

class OrderCreate(BaseModel):
    # TODO: user_id, restaurant_id, delivery_address_id, items: List[OrderItemIn]
    pass

class OrderUpdate(BaseModel):
    # TODO: status
    pass

class OrderOut(BaseModel):
    # TODO: id, user_id, restaurant_id, status, totals
    pass

from pydantic import BaseModel

class MenuItemCreate(BaseModel):
    # TODO: restaurant_id, name, description, price, is_available
    pass

class MenuItemUpdate(BaseModel):
    # TODO: optional fields
    pass

class MenuItemOut(BaseModel):
    # TODO: id, restaurant_id, name, price, is_available
    pass

from pydantic import BaseModel

class RestaurantCreate(BaseModel):
    # TODO: name, is_active
    pass

class RestaurantUpdate(BaseModel):
    # TODO: optional fields
    pass

class RestaurantOut(BaseModel):
    # TODO: id, name, is_active
    pass

from pydantic import BaseModel

class AddressCreate(BaseModel):
    # TODO: user_id, line1, line2, city, state, postal_code, country
    pass

class AddressUpdate(BaseModel):
    # TODO: optional fields
    pass

class AddressOut(BaseModel):
    # TODO: id, user_id, line1, ...
    pass

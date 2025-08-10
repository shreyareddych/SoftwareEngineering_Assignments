from pydantic import BaseModel

class UserCreate(BaseModel):
    # TODO: email, full_name, password
    pass

class UserUpdate(BaseModel):
    # TODO: optional fields
    pass

class UserOut(BaseModel):
    # TODO: id, email, full_name, is_active
    pass

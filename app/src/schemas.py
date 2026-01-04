from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    username: str = Field(..., min_length=3)
    email: str

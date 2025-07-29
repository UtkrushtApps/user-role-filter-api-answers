from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    username: str
    role: str
    status: str

    class Config:
        orm_mode = True

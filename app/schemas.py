from pydantic import BaseModel
from datetime import datetime


class FlyerBase(BaseModel):
    title: str
    description: str
    released: bool = True


class FlyerCreate(FlyerBase):
    pass


class Flyer(FlyerBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

from pydantic import BaseModel


class F1dataBase(BaseModel):
    name: str
    team: str
    points: int


class F1dataCreate(F1dataBase):
    pass


class F1data(F1dataBase):
    id: int

    class Config:
        orm_mode = True

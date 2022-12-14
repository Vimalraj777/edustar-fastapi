from pydantic import BaseModel
from typing import Optional


class Posts(BaseModel):
    id:str
    username:str
    password:str
    name:str
    age:str
    gender:str
    fname:str
    mname:str
    phnumber:int
    address:str


    class Config:
        orm_mode = True


class tokenData(BaseModel):
    id:Optional[str]=None
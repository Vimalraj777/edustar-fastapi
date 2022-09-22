from time import time
from pydantic import BaseModel
from typing import Optional
from pydantic import conint

class forgot(BaseModel):
    id:str
    username:str

class changePassword(BaseModel):
    otp:int
    id:str
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str
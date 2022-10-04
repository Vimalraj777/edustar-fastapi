from pydantic import BaseModel

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
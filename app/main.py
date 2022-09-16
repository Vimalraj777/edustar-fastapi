from fastapi.middleware.cors import CORSMiddleware
from . import oauth2
from fastapi import Body, FastAPI,Response,status,HTTPException
from random import randrange
from . import model
from .database import engine,Sessionlocal,get_db
from sqlalchemy.orm import Session , relationship
from fastapi import Depends
from . import schemas
from .utils import hash
from . import utils
from . import oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import func 
from .routers import post , user



oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')



# model.Base.metadata.create_all(bind=engine)


app=FastAPI()

origins=[
    "http://localhost:4200",
    "https://edustar-ui.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")
def test():
    return {"message":"Successfully registered"}


app.include_router(post.router)
app.include_router(user.router)

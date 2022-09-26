from random import randrange
from Databases.database import engine
from fastapi import Body, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy import func
from sqlalchemy.orm import Session, relationship
from Utils.utils import hash
from Controller.Routers import user , school

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


app.include_router(user.router)
app.include_router(school.router)

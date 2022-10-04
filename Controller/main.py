from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from Controller.Routers import user , school

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')



# model.Base.metadata.create_all(bind=engine)


app=FastAPI()

origins=[
    "http://localhost:4200",
    "https://edustar-ui.herokuapp.com",
    "https://dbstar-ui.herokuapp.com"
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

from http import client
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app import schemas
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , Session
from app.config import settings
from app.database import get_db
from app.database import Base
from app.oauth2 import create_access_token
# from .database import client , session 
# from fastapi import responses , requests


engine=create_engine(f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test")
TestingSessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)



client=TestClient(app)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db=TestingSessionlocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():    
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db]=override_get_db
    yield TestClient(app)
    

@pytest.fixture
def test_user(client):
    user_data={"id":"19297","username":"Vimal","password":"vimal@123","name":"Vimal Raj","age":20,"gender":"male","fname":"Charles","mname":"Saral","phnumber":6383279632,"address":"550A,East Street, Eleanganny."}
    res=client.post("/sqlalchemy",json=user_data)
    new_user=res.json()
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"Name":test_user['username']})

@pytest.fixture
def authorized_client(client,token):
    client.headers={
        **client.headers,
        "Authorization":f"Bearer {token}"
    }
    return client


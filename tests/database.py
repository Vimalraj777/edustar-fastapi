import token
from fastapi.testclient import TestClient
from app.database import get_db
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , Session
from app.config import settings
from app import schemas
from app.model import Base
# import pytest
from app.oauth2 import create_access_token



engine=create_engine(f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test")
TestingSessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
# Base.metadata.create_all(bind=engine)
Base=declarative_base()

def override_get_db():
    db=TestingSessionlocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db]=override_get_db

client=TestClient(app)


@pytest.fixture(scope="module")
def session():
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    db=TestingSessionlocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client(session):
    def override_get_db(): 
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db]=override_get_db
    yield TestClient(app)

# @pytest.fixture
# def authorized_client(client,token):
#     client.headers={
#         **client.headers , "Authorization":f"Bearer{token}"
#     }
#     return client


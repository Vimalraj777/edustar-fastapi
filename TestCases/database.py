import pytest
from fastapi.testclient import TestClient
from Controller.main import app
from ..Schema import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..Configuration.config import settings
from ..Databases.database import get_db
from ..Databases.database import Base


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
    
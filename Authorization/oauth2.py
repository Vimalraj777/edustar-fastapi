import importlib
from jose import JWTError , jwt
from datetime import datetime , timedelta
from Schema import schemas 
from fastapi import Depends
from fastapi import HTTPException , status
from fastapi.security.oauth2 import OAuth2PasswordBearer 
from Model import school_profile , user_profile
from sqlalchemy.orm import Session
from Databases.database import get_db
from Configuration.config import settings

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='Login')


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data:dict):
    encoded=data.copy()
    expire=datetime.utcnow()+timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    encoded.update({'exp':expire})
    encoded_jwt=jwt.encode(encoded,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token:str,credential_exception):
    print("token :",token)
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    id:str=payload.get("Name")
    if id is None:
        raise credential_exception
    token_data=schemas.tokenData(id=id)
    return token_data


def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credential_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail=f"could not authenticate credentials")
    user= verify_token(token,credential_exception)
    print("data",user)
    cur_user=db.query(user_profile.School).filter(user_profile.School.username==user.id).first() 
    print(cur_user.id)
    return cur_user
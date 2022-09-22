import pytest
from jose import jwt
from Configuration.config import settings


def test_login_user(client , test_user):
    res=client.post("/Login",data={"username":test_user['username'],"password":test_user['password']})
    new=res.json()
    payload=jwt.decode(new['token'],settings.secret_key,algorithms=[settings.algorithm])
    user_name=payload.get('Name')
    assert user_name==test_user['username']
    assert res.status_code==200   # since i am not raising error in main.py instead i am returning that's why status code 200
    print(new['token'])

def test_incorrect_login(client,test_user):
    res=client.post("/Login",data={"username":"vimal","password":test_user['password']})
    assert res.status_code==404
    assert res.json().get('detail')=="invalid credentials"
    

def test_root(client):
    res=client.get('/')
    print(res.json().get('message'))




from app import schemas
from .database import client , session 
from fastapi import responses , requests
    





def test_root():
    print("successfully")
    res=client.__get__('message')
    print(res)

def test_login_user(client):
    res=client.post("/Login",data={'username':'Vimal','password':'vimal@123'})
    print(res.json())
    assert res.status_code == 200

# def test_get_token(authorized_client):
#     res=authorized_client.__get__('/getdata')
#     print(res)

def test_get_all_posts(authorized_client):
    res=authorized_client.get("/profile")
    assert res.status_code==200
    print(res.json())

def test_get_posts_unauthorized(client):
    res=client.get("/profile")
    assert res.status_code==401
    print(res.json())

def test_put_post(authorized_client,test_user):
    res=authorized_client.put("/sqlalchemy",json={"id":"19297","username":"Vimal Raj","password":"vimal@123","name":"Vimal Raj","age":20,"gender":"male","fname":"Charles","mname":"Saral","phnumber":6383279632,"address":"550A,East Street, Eleanganny."})
    print(res.status_code)
    assert res.json().get('id')==test_user['id']



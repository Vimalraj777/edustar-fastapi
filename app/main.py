# from asyncio.windows_events import NULL
# import re
# from cmath import log
from operator import mod
from fastapi.middleware.cors import CORSMiddleware
# from typing import Optional
# from urllib import response
# from colorama import Cursor
from . import oauth2
from fastapi import Body, FastAPI,Response,status,HTTPException
from random import randrange
import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
from . import model
from .database import engine,Sessionlocal,get_db
from sqlalchemy.orm import Session , relationship
from fastapi import Depends
from .schemas import Posts,Log,users,Token , tokenData ,POSTS , create , Vote
from .utils import hash
# from . import utils
from . import oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import func 


# access_token=oauth2.create_access_token(data={'user_id':users.id})
# return {"token":access_token}
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')



model.Base.metadata.create_all(bind=engine)


app=FastAPI()
origins=[
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/Login")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    data1=db.query(model.School).filter(model.School.username==user_credentials.username).first()
    if data1:
        data2=db.query(model.School).filter(model.School.password==user_credentials.password).first()
        if data2:
            access_token=oauth2.create_access_token(data={"Name":user_credentials.username})
            return {"token":access_token}       
        c= HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
        return c
    b= HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    return b


@app.get("/getdata")
def test_post(db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    return user  






#register for school profile
@app.post("/sqlalchemy") 
def crate_post(post:Posts,db:Session=Depends(get_db)):
    new_post=model.School( **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return "Success"


#retrieve values for school profile
@app.get("/profile")
def test_post(db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    new_post=db.query(model.School).filter(model.School.id==user_id.id)
    new=new_post.first()
    return new




#update school profile
@app.put("/sqlalchemy")
def updated(post:Posts,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    updated_post=db.query(model.School).filter(model.School.id==user.id)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    updated_post.update(post.dict(),synchronize_session=False)  
    db.commit()
    return {"id":up.id}



def setData(data):
    key=[]
    get=[]
    set=[]
    for list in data:
        key =list.keys()
        break
    for list in data:
        for value in key:
            get.append(list[value])
        set.append(get)
        get=[]
    return set        





# post records for edustar project
@app.post("/post") 
def crate_post(post:dict,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    post['scholarship']=setData(post['scholarship'])
    # print(post['scholarship'])
    new_post=model.Information( **post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post.id}




# get specific record for edustar project
@app.get("/get/{id}")
def test_post(id:int,db:Session=Depends(get_db)):
    new_post=db.query(model.Information).filter(model.Information.id==id)
    new=new_post.first()
    return {"data":new}



@app.get("/profileget")
def test_post(db:Session=Depends(get_db),user_id:str=Depends(oauth2.get_current_user)):
    new_post=db.query(model.Information).filter(model.Information.id==user_id.id)
    new=new_post.first()
    return new



# update the retrieved edustar details record.
@app.put("/profileput")
def updated(post:dict,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    updated_post=db.query(model.Information).filter(model.Information.id==user.id)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    post['scholarship']=setData(post['scholarship'])
    updated_post.update(post,synchronize_session=False)
    db.commit()
    return {"id":up.id}


@app.delete("/deleted")
def delete_post(db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    new_post=db.query(model.School).filter(model.School.id==user.id)
    if new_post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    new_post.delete(synchronize_session=False)
    db.commit()   
    return Response(status_code=status.HTTP_204_NO_CONTENT)




# get all records from Edustar General Information Table
@app.get("/get")
def test_post(db:Session=Depends(get_db)):
    new_post=db.query(model.Information).all()
    return new_post



    
     
# display user profile
@app.get("/sqlalchemy")
def test_post(db:Session=Depends(get_db)):
    new_post=db.query(model.School).all()
    return new_post


@app.get("/")
def test():
    return {"message":"Successfully registered"}







#update the purticular post
'''@app.put("/posts/{id}")
def update(id:int,post:Cl):
    index=find_index(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"There no id {id}")
    post_dict=post.dict()
    post_dict["id"]=id
    my_posts[index]=post_dict
    return{"msg":my_posts}'''

# Connecting database


'''@app.delete("/sqlalchemy/{id}")
def delete_post(id:int,db:Session=Depends(get_db)):
    new_post=db.query(model.Product).filter(model.Product.id==id)
    if new_post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    new_post.delete(synchronize_session=False)
    db.commit()   
    return response(status_code=status.HTTP_204_NO_CONTENT)'''

 
@app.post("/user")
def login(post:users,db:Session=Depends(get_db)):
    hashed=hash(post.id)
    post.id=hashed
    new=model.Login(**post.dict())
    db.add(new)
    db.commit()
    return {"data":"successful"}


@app.post("/sample") 
def crate_post(post:POSTS,db:Session=Depends(get_db)):
    print('works')
    new_post=model.Sample( **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post}









@app.post("/sendposts") 
def crate_post(post:create,db:Session=Depends(get_db) , user_id:int=Depends(oauth2.get_current_user)):
    new_post=model.Posts( **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post}




@app.get("/gettoken")
def test_post(db:Session=Depends(get_db), user_id:int=Depends(oauth2.get_current_user)):
    # new_post=db.query(model.Posts).filter(model.Posts.user_id==user_id.id).all()
    posts=db.query(model.Posts,func.Count(model.Vote.posts_id).label("votes")).join(model.Vote,model.Vote.posts_id==model.Posts.id).group_by(model.Posts.id).filter(model.Posts.user_id==user_id.id).all()
    return posts



@app.put("/puttoken")
def updated(post:create,db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    updated_post=db.query(model.Posts).filter(model.Posts.user_id==user_id.id)
    up=updated_post.first()
    # print(up)
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    # update_post=db.query(model.Posts).filter(model.Posts.user_id==user_id.id)
    updated_post.update(post.dict(),synchronize_session=False)
    db.commit()
    return {"id":up.id}






@app.post("/vote" )
def vote(vote:Vote,db:Session=Depends(get_db),current_user:int =Depends(oauth2.get_current_user)):
    vote_query=db.query(model.Vote).filter(model.Vote.posts_id==vote.posts_id,model.Vote.users_id==current_user.id)
    found_vote=vote_query.first()
    if(vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user{current_user.id} has already liked for post{vote.posts_id}")
        new_vote=model.Vote(posts_id=vote.posts_id,users_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"Successfully added vote"}

    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user {current_user.id} didn't liked post")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message":"Deleted vote Successfully"}


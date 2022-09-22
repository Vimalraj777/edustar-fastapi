from ctypes.wintypes import PINT
from pickle import GLOBAL
from typing import Set
from fastapi import status,HTTPException , APIRouter , Depends
from sqlalchemy.orm import Session , relationship
from Utils import utils
from Databases.database import get_db
# from Model import user_profile
from Model import school_profile
from Schema import school_schema
from Authorization import oauth2



router=APIRouter(
    tags=['Users']
)


def set_data(data):
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



# post records for edustar School Profile
@router.post("/post") 
def crate_post(post:dict,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    post['scholarship']=set_data(post['scholarship'])
    post['enrollment']=set_data(post['enrollment'])
    # print(post['scholarship'])
    new_post=school_profile.Information( **post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post.id}



@router.get("/profileget")
def test_post(db:Session=Depends(get_db),user_id:str=Depends(oauth2.get_current_user)):
    new_post=db.query(school_profile.Information).filter(school_profile.Information.id==user_id.id)
    new=new_post.first()
    return new


# update the retrieved edustar School Profile details record.
@router.put("/profileput")
def updated(post:dict,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    updated_post=db.query(school_profile.Information).filter(school_profile.Information.id==user.id)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    post['scholarship']=set_data(post['scholarship'])
    post['enrollment']=set_data(post["enrollment"])
    updated_post.update(post,synchronize_session=False)
    db.commit()
    return {"id":up.id}



# get specific record for edustar  School Profile project
@router.get("/get/{id}")
def test_post(id:int,db:Session=Depends(get_db)):
    new_post=db.query(school_profile.Information).filter(school_profile.Information.id==id)
    new=new_post.first()
    return {"data":new}


# get all records from Edustar School Profile 
@router.get("/get")
def test_post(db:Session=Depends(get_db)):
    new_post=db.query(school_profile.Information).all()
    return new_post


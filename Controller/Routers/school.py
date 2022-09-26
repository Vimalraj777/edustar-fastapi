from ctypes.wintypes import PINT
from pickle import GLOBAL
from typing import Set
from fastapi import status,HTTPException , APIRouter , Depends
from sqlalchemy.orm import Session , relationship
from Utils import utils
from Databases.database import get_db
# from Model import user_profile
from Model import school_model
from Schema import school_schema
from Authorization import oauth2



router=APIRouter(
    tags=['Users']
)

# a function to split the value alone as a list from a dictionary 
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



# Insert the data of school Profile
@router.post("/post") 
def crate_post(post:dict,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    post['scholarship']=set_data(post['scholarship'])
    post['enrollment']=set_data(post['enrollment'])
    # print(post['scholarship'])
    new_post=school_model.Information( **post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post.id}



# This method is used to get the logged in user's record from 'School Profile' Data Table.
@router.get("/profileget")
def test_post(db:Session=Depends(get_db),user_id:str=Depends(oauth2.get_current_user)):
    user_id.id=str(user_id.id)
    new_post=db.query(school_model.Information).filter(school_model.Information.id==user_id.id)
    new=new_post.first()
    print(new)
    return new


# This method is used to update the School Profile's record.
@router.put("/profileput") 
def updated(post:dict,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    user.id=str(user.id)
    updated_post=db.query(school_model.Information).filter(school_model.Information.id==user.id)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    post['scholarship']=set_data(post['scholarship'])
    post['enrollment']=set_data(post["enrollment"])
    updated_post.update(post,synchronize_session=False)
    db.commit()
    return {"id":up.id}



# This method is used to get Specific record from 'School Profile' Data table without Token Validation
@router.get("/get/{id}")
def test_post(id:int,db:Session=Depends(get_db)):
    new_post=db.query(school_model.Information).filter(school_model.Information.id==id)
    new=new_post.first()
    return {"data":new}


# get all records from  'School Profile' Table. 
@router.get("/get")
def test_post(db:Session=Depends(get_db)):
    new_post=db.query(school_model.Information).all()
    return new_post


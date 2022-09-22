from ctypes.wintypes import PINT
from pickle import GLOBAL
from typing import Set
from fastapi import Body, FastAPI,Response,status,HTTPException , APIRouter , Depends
from sqlalchemy.orm import Session , relationship
from Utils import utils
from Databases.database import get_db
from Model import user_profile
from Model import school_profile
from Schema import schemas
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Authorization import oauth2
import random



router=APIRouter(
    tags=['Users']
)


pin=[]
@router.post("/forgot")
def forgot(post:schemas.forgot,db:Session=Depends(get_db)):
    data1=db.query(user_profile.School).filter(user_profile.School.id==post.id , user_profile.School.username==post.username)
    if data1.first():
        data={}
        index = -1
        rand=random.randint(111111,999999)
        if pin != []:
            for i in range(len(pin)):
                if pin[i]['id'] == post.id:
                    index = i

            if index != -1:
                pin[index]['pin'] = rand
            else:    
                data={'id':post.id,'pin':rand}
                pin.append(data)
        else:
            data={'id':post.id,'pin':rand}
            pin.append(data)    

        print(pin)
        for i in range(len(pin)):
                if pin[i]['id'] == post.id:
                    index = i
        return pin[index]['pin']
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid RollNo or Username")



@router.post("/change")
def change_password(post:schemas.changePassword,db:Session=Depends(get_db)):
        data1=db.query(user_profile.School).filter(user_profile.School.id==post.id)
        if data1.first():
            print("yes",pin)
            for i in range(len(pin)):
                print(i)
                if pin[i]['id'] == post.id:
                    if pin[i]['pin']==post.otp:
                        data1.update({'password':post.password},synchronize_session=False)
                        db.commit()
                        return data1.first()
                    else:
                        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid OTP")
                else:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Generate Your OTP first!!")
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid!!!")





@router.post("/Login")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    data1=db.query(user_profile.School).filter(user_profile.School.username==user_credentials.username).first()
    if data1:
        data2=db.query(user_profile.School).filter(user_profile.School.password==user_credentials.password).first()
        if data2:
            access_token=oauth2.create_access_token(data={"Name":user_credentials.username})
            return {"token":access_token}       
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    



        
   


@router.get("/getdata")
def test_post(db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    return user  



#register for user profile
@router.post("/sqlalchemy") 
def register(post:schemas.Posts,db:Session=Depends(get_db)):
    new_post=user_profile.School( **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


#retrieve values for user profile
@router.get("/profile")
def get_registers(db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    new_post=db.query(user_profile.School).filter(user_profile.School.id==user_id.id)
    new=new_post.first()
    return new


#update user profile
@router.put("/sqlalchemy")
def updated(post:schemas.Posts,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    updated_post=db.query(user_profile.School).filter(user_profile.School.id==user.id)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    updated_post.update(post.dict(),synchronize_session=False)  
    db.commit()
    return {"id":up.id}


#delete user profile unique record by id
@router.delete("/deleted")
def delete_post(db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    new_post=db.query(user_profile.School).filter(user_profile.School.id==user.id)
    if new_post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    new_post.delete(synchronize_session=False)
    db.commit()   
    return Response(status_code=status.HTTP_204_NO_CONTENT)


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



# post records for edustar School Profile
@router.post("/post") 
def crate_post(post:dict,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    post['scholarship']=setData(post['scholarship'])
    post['enrollment']=setData(post['enrollment'])
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
    post['scholarship']=setData(post['scholarship'])
    post['enrollment']=setData(post["enrollment"])
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


     
# display user profile
@router.get("/sqlalchemy")
def test_post(db:Session=Depends(get_db)):
    new_post=db.query(user_profile.School).all()
    return new_post
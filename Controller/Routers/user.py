from ctypes.wintypes import PINT
from pickle import GLOBAL
from typing import Set
from fastapi import Response,status,HTTPException , APIRouter , Depends
from sqlalchemy.orm import Session , relationship
from Utils import utils
from Databases.database import get_db
from Model import user_model , school_model
from Schema import login_schema , user_schema
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Authorization import oauth2
import random



router=APIRouter(
    tags=['Users']
)


pin=[]
@router.post("/forgotpassword")
def forgot(post:login_schema.forgot,db:Session=Depends(get_db)):
    data1=db.query(user_model.School).filter(user_model.School.id==post.id , user_model.School.username==post.username)
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



@router.post("/changepassword")
def change_password(post:login_schema.changePassword,db:Session=Depends(get_db)):
        data1=db.query(user_model.School).filter(user_model.School.id==post.id)
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
    data1=db.query(user_model.School).filter(user_model.School.username==user_credentials.username).first()
    if data1:
        data2=db.query(user_model.School).filter(user_model.School.password==user_credentials.password).first()
        if data2:
            access_token=oauth2.create_access_token(data={"Name":user_credentials.username})
            return {"token":access_token}       
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="invalid credentials")
    



        
   


@router.get("/getdata")
def test_post(db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    return user  



#register for user profile
@router.post("/register") 
def register(post:user_schema.Posts,db:Session=Depends(get_db)):
    new_post=user_model.School( **post.dict())
    db.add(new_post)
    check=db.query(school_model.Information).filter(school_model.Information.id==post.id)
    if not check.first():
        school_record=school_model.Information(id=post.id)
        db.add(school_record)
        print(school_record)
    db.commit()
    db.refresh(new_post)
    return new_post


#retrieve values for user profile
@router.get("/getuser")
def get_registers(db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    new_post=db.query(user_model.School).filter(user_model.School.id==user_id.id)
    new=new_post.first()
    return new


#update user profile
@router.put("/updateUser")
def updated(post:user_schema.Posts,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    updated_post=db.query(user_model.School).filter(user_model.School.id==user.id)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    updated_post.update(post.dict(),synchronize_session=False)  
    db.commit()
    return {"id":up.id}


#delete user profile unique record by id
@router.delete("/deleteUser")
def delete_post(db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    new_post=db.query(user_model.School).filter(user_model.School.id==user.id)
    if new_post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    new_post.delete(synchronize_session=False)
    db.commit()   
    return Response(status_code=status.HTTP_204_NO_CONTENT)

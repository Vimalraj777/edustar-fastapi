from fastapi import Body, FastAPI,Response,status,HTTPException , APIRouter , Depends
from sqlalchemy.orm import Session , relationship
from ..database import get_db
from .. import model , schemas , utils
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import oauth2



router=APIRouter(
    tags=['Users']
)

@router.post("/Login")
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    data1=db.query(model.School).filter(model.School.username==user_credentials.username).first()
    if data1:
        data2=db.query(model.School).filter(model.School.password==user_credentials.password).first()
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
    new_post=model.School( **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


#retrieve values for user profile
@router.get("/profile")
def get_registers(db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    new_post=db.query(model.School).filter(model.School.id==user_id.id)
    new=new_post.first()
    return new


#update user profile
@router.put("/sqlalchemy")
def updated(post:schemas.Posts,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    updated_post=db.query(model.School).filter(model.School.id==user.id)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    updated_post.update(post.dict(),synchronize_session=False)  
    db.commit()
    return {"id":up.id}


#delete user profile unique record by id
@router.delete("/deleted")
def delete_post(db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    new_post=db.query(model.School).filter(model.School.id==user.id)
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
    new_post=model.Information( **post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post.id}



@router.get("/profileget")
def test_post(db:Session=Depends(get_db),user_id:str=Depends(oauth2.get_current_user)):
    new_post=db.query(model.Information).filter(model.Information.id==user_id.id)
    new=new_post.first()
    return new


# update the retrieved edustar School Profile details record.
@router.put("/profileput")
def updated(post:dict,db:Session=Depends(get_db), user=Depends(oauth2.get_current_user)):
    updated_post=db.query(model.Information).filter(model.Information.id==user.id)
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
    new_post=db.query(model.Information).filter(model.Information.id==id)
    new=new_post.first()
    return {"data":new}


# get all records from Edustar School Profile 
@router.get("/get")
def test_post(db:Session=Depends(get_db)):
    new_post=db.query(model.Information).all()
    return new_post


     
# display user profile
@router.get("/sqlalchemy")
def test_post(db:Session=Depends(get_db)):
    new_post=db.query(model.School).all()
    return new_post
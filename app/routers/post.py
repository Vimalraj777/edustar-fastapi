from fastapi import status,HTTPException,Depends , APIRouter
from sqlalchemy.orm import Session , relationship
from ..database import get_db
from .. import model , schemas 
from .. import oauth2
from sqlalchemy import func 



router=APIRouter(
    tags=['Posts']
)

@router.post("/sendposts") 
def crate_post(post:schemas.create,db:Session=Depends(get_db) , user_id:int=Depends(oauth2.get_current_user)):
    new_post=model.Posts( **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post}


@router.get("/gettoken")
def test_post(db:Session=Depends(get_db), user_id:int=Depends(oauth2.get_current_user)):
    posts=db.query(model.Posts,func.Count(model.Vote.posts_id).label("votes")).join(model.Vote,model.Vote.posts_id==model.Posts.id).group_by(model.Posts.id).filter(model.Posts.user_id==user_id.id).all()
    return posts



@router.put("/puttoken")
def updated(post:schemas.create,db:Session=Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    updated_post=db.query(model.Posts).filter(model.Posts.user_id==user_id.id)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    updated_post.update(post.dict(),synchronize_session=False)
    db.commit()
    return {"id":up.id}


@router.post("/user")
def posts(post:schemas.user,db:Session=Depends(get_db)):
    new=model.Log(**post.dict())
    db.add(new)
    db.commit()
    return {"data":"successful posted"}




@router.post("/vote" )
def vote(vote:schemas.Vote,db:Session=Depends(get_db),current_user:int =Depends(oauth2.get_current_user)):
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
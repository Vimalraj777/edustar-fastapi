from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,ARRAY , BigInteger
from Databases.database import Base
from sqlalchemy.orm import relationship



class School(Base):
    __tablename__="studentdata"
    id=Column(String,nullable=False,primary_key=True)
    username=Column(String,nullable=False)
    password=Column(String,nullable=False)
    name=Column(String,nullable=False)
    age=Column(Integer,nullable=False)
    gender=Column(String,nullable=False)
    fname=Column(String,nullable=False)
    mname=Column(String,nullable=False)
    phnumber=Column(BigInteger,nullable=False)
    address=Column(String,nullable=False)
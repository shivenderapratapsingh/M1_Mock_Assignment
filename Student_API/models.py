from sqlalchemy import Column,Integer,String
from database import Base

class Student(Base):
    __tablename__="students"

    s_id=Column(Integer,primary_key=True,index=True)
    s_name=Column(String,index=True)
    s_age=Column(Integer)
    s_course=Column(String)
    s_college=Column(String)


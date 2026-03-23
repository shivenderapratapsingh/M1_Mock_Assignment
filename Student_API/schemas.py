from typing import Optional

from pydantic import BaseModel


class StudentCreate(BaseModel):
    s_name: str
    s_age: int
    s_course: str
    s_college: str

class StudentUpdate(BaseModel):

    s_name: Optional[str] = None
    s_age: Optional[int] = None
    s_course: Optional[str] = None
    s_college: Optional[str] = None

class StudentResponse(BaseModel):
    s_id: int
    s_name: str
    s_age: int
    s_course: str
    s_college: str

    class Config:
        from_attributes = True   # important for ORM compatibility
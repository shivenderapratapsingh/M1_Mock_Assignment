from typing import List

from fastapi import FastAPI,Depends, HTTPException,status
from sqlalchemy.orm import Session
from database import SessionLocal,engine,Base
from models import Student
from schemas import StudentCreate,StudentResponse, StudentUpdate

app=FastAPI()
 
Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students")
def create_student(student:StudentCreate,db:Session=Depends(get_db)):
    if student.s_age < 0:
        raise HTTPException(status_code=400, detail="Invalid age")
    student=Student(s_name=student.s_name,s_age=student.s_age,s_course=student.s_course,s_college=student.s_college)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.get("/students", response_model=List[StudentResponse])
def read_students(db:Session=Depends(get_db)):
     students=db.query(Student).all()
     if not students:   # empty list check
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No students found"
        )
     return students

@app.delete("/students/{student_id}")
def delete_student(student_id:int,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.s_id==student_id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student Not found"
        )
    db.delete(student)
    db.commit()
    return {
        "message":"Student deleted"
    }


@app.put("/students/{id}", response_model=StudentResponse)
def update_student(
    id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):

    existing_student = db.query(Student).filter(Student.s_id == id).first()

    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student.model_dump(exclude_unset=True).items():
        setattr(existing_student, key, value)

    db.commit()
    db.refresh(existing_student)

    return existing_student

@app.get("/student/{student_id}",response_model=StudentResponse)
def get_by_id(student_id:int,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.s_id==student_id).first()
    if not student:
        raise HTTPException(
            status_code=404,detail="Student not found"
        )
    return student

from typing import List, Optional

@app.get("/students", response_model=List[StudentResponse])
def read_students(
    course: Optional[str] = None,
    db: Session = Depends(get_db)
):

    query = db.query(Student)

    if course:
        query = query.filter(Student.s_course == course)

    students = query.all()

    if not students:
        raise HTTPException(
            status_code=404,
            detail="No students found"
        )

    return students
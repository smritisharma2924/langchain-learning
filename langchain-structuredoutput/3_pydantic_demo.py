from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'unknown'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)

new_student = {'name':'smriti', 'age':'19', 'email':'ss@gmail.com', 'cgpa':8.36}

student = Student(**new_student)

print(student)
print(type(student))
from pydantic import BaseModel, confloat, validator
import uuid 
from datetime import date, datetime, timedelta 
from enums import DepartmentEnum 


class Student(BaseModel):
    id: uuid.UUID 
    name: str 
    date_of_birth: date
    gpa: confloat(gt=0, lt=4)
    course: str | None # If you are using python 3.9 or below use Union[str, None]
    department: DepartmentEnum
    fees_paid: bool 

    # we can write custom validator for specific field
    @validator('date_of_birth')
    def ensure_16_or_over(cls, value):
        sixteen_years_ago = datetime.now() - timedelta(days=365*16)
        sixteen_years_ago = sixteen_years_ago.date()

        if value > sixteen_years_ago:
            raise ValueError('Too young to enrol, sorry')
        return value 
    

# Constrained Types 
# u1 = {'name': 'xyz', 'age': 50}
# u2 = {'name': 'abc', 'age': 140}

# class User(BaseModel):
#     name: str 
#     age: conint(gt=0, lt=100)

# # attempt to convert to Pydantic model 
# user1 = User(**u1)
# user2 = User(**u2)
# print(user2)
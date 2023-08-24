from pydantic import BaseModel, confloat, validator, Field
# Literal will allow you to define to the set of values you gave to Literal
from typing import Literal 
import uuid 
from datetime import date, datetime, timedelta 
from enums import DepartmentEnum 


class Module(BaseModel):
    id: int | uuid.UUID 
    name: str 
    professor: str 
    # Module have credits which can be 10 or 20 only. We will not allow any other integer number
    credits: Literal[10, 20] 
    registration_code: str 

# what if we want to call the name of the pydantic model different than the field in source data
# we can do like this

# student_name: str = Field(alias="name")
class Student(BaseModel):
    id: uuid.UUID = Field()
    name: str 
    date_of_birth: date = Field(default_factory=lambda: datetime.today().date())
    GPA: confloat(gt=0, lt=4)
    course: str | None # If you are using python 3.9 or below use Union[str, None]
    department: DepartmentEnum
    fees_paid: bool 
    # modules: list[Module] = []
    modules: list[Module] = Field(default=[], max_items=10)


    # we can write custom validator for specific field
    @validator('modules') 
    def validate_module_length(cls, value):
        if len(value) and len(value) !=3:
            raise ValueError('List of modules should have length 3')
        return value 
    
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

# Exporting models into dictionary or json
# two additional arguments are 
# include and exclude
# Lets say we want to exclude the list of modules from the output data

# class Student(BaseModel):
#     modules = list[Module] = Field(default=[], exclude=True)

# If you have several field for which you want to exclude, instead of referring
# to each of them you can set the exlude in model_dump of the output like this

# print(model.dump(exclude={'id','module'}))




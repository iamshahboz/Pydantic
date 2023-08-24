import requests 
from models import Student, Module
import json 
from pprint import pprint


url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'

response = requests.get(url)
data = response.json()

# field customization pydantic 19:56

# we can append dummy data to ensure that our custom validation is working properly

# data.append(
#     {
#         "id": "48dda775-785d-41e3-b0dd-26a4a2f7722f",
#         "name": "Justin Holden",
#         "date_of_birth": "2010-08-22",
#         "GPA": "3.23",
#         "course": "Philosophy",
#         "department": "Arts and Humanities",
#         "fees_paid": 'true'
#     }
# )

# since we appended the item which credit value is 24 we are getting validation error
# after module length validation when we try to append one more elemen
# data[-1]['modules'].append(
#     {
#         "id": 101,
#         "name": "Japanese Cinema",
#         "professor": "Prof. Travis Hudson",
#         "credits": 20,
#         "registration_code": "abc"
#     }
# )

del data[-1]["date_of_birth"]

for student in data:
    model = Student(**student)
# now we can iterate over the module. Remember it is the field of Student model
    # for module in model.modules:
    #     # since the id field is the union of id and uuid we get both and no error
    #     print(module.id)

# and if we have a nested module we can exclude the specific field like this
    # excludes = {
    #     "id": True,
    #     "modules": {"__all__": {"registration_code"}}
    # }
    # pprint(model.model_dump(exclude=excludes))

    # print(model.model_dump(exclude={'id','modules','fees_paid'}))
    





# Lets look at something called json schema. It is a declarative language that allows
# you to annotate and validate JSON documents 
# Now we can learn how to take Pydantic model and convert it to JSON Schema

# print(Module.schema_json(indent=2))
# print(json.dumps(Module.model_json_schema(),indent=2))
# print(json.dumps(Student.model_json_schema(),indent=2))

# now we can do something reverse, for instance we are given a json file and we want to
# convert it back to Pydantic model. For that we can use a library called
# datamodel-code-generator

# this library provides a command line tool called 
# datamodel-codegen --input (you should input your file) --output models.py

# while generating keep in mind that custom validations will not be taken into consideration






        


    
    







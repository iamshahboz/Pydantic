import requests 
from pprint import pprint
from schemas import Student


url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v1.json'

response = requests.get(url)
data = response.json()

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


for student in data:
    model = Student(**student)
    pprint((model.model_dump_json()))
    
    







import json
import requests

def testCode():
    json_obj = ""
    with open('sample.json','r') as file:
        json_obj=json.load(file)
    print(type(json_obj))

    print(requests.post(
        "http://127.0.0.1:8000/",
        json.load(json_obj)
        ).json())
    
testCode()
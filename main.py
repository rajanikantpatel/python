from enum import Enum
from fastapi import FastAPI 
#from pydentic import BaseModel
import json


app = FastAPI()

@app.post("/")
def cacluateTotalPaintArea(json_obj):
    # with open('sample.json','r') as file:
    #     json_obj=json.load(file)
    #     print(json_obj)
    heigth = json_obj['heigth']

    def areaCaclulator(area) -> json :
        excludeArea = 0.0
        includeAreaWall = 0.0
        includeAreaCeiling = 0.0
        for room in range(len(area)):
            for win in range(len(area[room]['windows'])):
                    excludeArea+=(area[room]['windows'][win]['heigth'])*(area[room]['windows'][win]['width'])
            includeAreaWall = 2*heigth*area[room]['length']+2*heigth*area[room]['width']+area[room]['width']*area[room]['length']
            includeAreaCeiling = area[room]['width']*area[room]['length']
        
        totalAreaWall = includeAreaWall - excludeArea
        return {'includeAreaWall': totalAreaWall, 'totalAreaCeiling': includeAreaCeiling}
    
    wall=0.0
    ceiling=0.0
    for type in ['kitchen-size','hall-size','bedrooms-size']:
         response=areaCaclulator(json_obj[type])
         wall+=response['includeAreaWall']
         ceiling+=response['totalAreaCeiling']
    
    return {'wall': wall, 'ceiling': ceiling}


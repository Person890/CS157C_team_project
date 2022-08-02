import pandas as pd
from pymongo import MongoClient
import json

client = MongoClient("mongodb://54.198.141.68:27021")
db = client.police

# Creating an array with the name of all files
str_start = "policecalls/policecalls20"
str_end = ".csv"
yrs = ["13","14","15","16","17","18","19","20","21","22"]
for yr in yrs:
    file = str(str_start + yr + str_end)
    data = pd.read_csv(file)
    payload = json.loads(data.to_json(orient='records'))
    print("about to insert file for 20"+ yr)
    db.policeData.insert_many(payload)

client.close()
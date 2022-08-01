
from datetime import date, datetime
from pymongo import MongoClient
import pandas as pd
import json

client = MongoClient("mongodb://54.226.206.216:27021")
db = client.police

# for data in db.policeData.find().limit(2):
#     print(data)

q = False
while(not q):
    # Menu ---
    print('Police Call Data for the City of San Jose')
    print()
    print('Enter (Q)uit at any time to exit the application')
    print()
    print('Choose a function from the menu by entering the corresponding number')
    print('(1) RecordCall')
    print('(2) ReturnCallNumber')
    print('(3) UpdateCall')
    print('(4) ReturnCallDetails')
    print('(5) CallsbyDate')
    print('(6) CallsbyEmp')
    print('(7) AggregateCallsPerDay')
    print('(8) AggregateCallsPerCallType')
    print('(9) DeleteCallsByType')
    print('(10) DeleteCallsByNumber')
    print()
    # --- end menu
    # get user choice
    user = input('Select now or (Q)uit: ')
    # check for exit
    if str(user).lower() == 'q':
        q = True
    elif str(user) == '1':
    #    def record_call():
            dateinput = input('Type start date in format: "MM/DD/YYYY": ')
            timeinput = input('Type time in format "00:00:00": ')
            calltypeinput = input('Type in the type of call: ')
            cityinput = input('Type in the city (location) of the call: ')
            documentInsert = [
                {"OFFENSE_DATE": dateinput, "OFFENSE_TIME": timeinput, "CALL_TYPE": calltypeinput, "CITY": cityinput}]
            x = db.policeData.insert_many(documentInsert);
            print('Insert OK')
            for data in db.policeData.find({},{"CDTS": 0, "EID": 0, "CALL_NUMBER": 0, "PRIORITY": 0, 'REPORT_DATE': 0, 'OFFENSE_DATE': 0, 'CALLTYPE_CODE': 0, 'FINAL_DISPO_CODE': 0, 'FINAL_DISPO': 0, 'COMMON_PLACE_NAME': 0}):
                print(data)
    elif str(user) == '2':
        # def return_call_number():

            callTypeInput = input('Please type the call type (STOLEN VEHICLE, PERSON DOWN,...): ')
            myquery = { "CALL_TYPE": callTypeInput}
            mydoc = db.policeData.find(myquery)

    elif str(user) == '3':
        # def update_call():
            print("you pressed 3")
       
    elif str(user) == '4':
        # def return_call_details():
            idInput = input("Type in the ID of the call: ")
            myquery = { "_id": idInput }
            mydoc = db.policeData.find(myquery)

    elif str(user) == '5':
        # def calls_by_date():
            print("This query will take in starting and ending dates and return calls within the range.")
            gteInput = input("Type in starting date: ")
            lteInput = input("Type in ending date: ")
            myquery = {"START_DATE": {"$gte": gteInput}, "START_DATE": {"$lte": lteInput},}
            mydoc = db.policeData.find(myquery) 

    elif str(user) == '6':
        # def calls_by_emp():
            print("This query will take in employee ID and will return calls of that employee.")
            eidInput = input("Type in the employee ID: ")
            narrowByDate = input("Do you want to narrow the search by date? (Y/N)")
            if (narrowByDate == 'Y'):
                gteInput = input("Type in starting date: ")
                lteInput = input("Type in ending date: ")
                myquery = {"EID": eidInput, "START_DATE": {"$gte": gteInput}, "START_DATE": {"$lte": lteInput},}
                mydoc = db.policeData.find(myquery) 

    elif str(user) == '7':
        # def aggregate_calls_per_day():
            print("Hello from a function")

    elif str(user) == '8':
        # def aggregate_calls_per_call_type():
            print("Hello from a function")

    elif str(user) == '9':
        # def delete_calls_by_type():
            print("Hello from a function")

    elif str(user) == '10':
        # def delte_calls_by_call_number():
            print("Hello from a function")
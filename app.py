from pymongo import MongoClient

# functions
# function 1
def record_call():
    print('')
    print('--- Record (insert) a New Call ---')
    dateinput = input('Type offense date in format: "MM/DD/YYYY": ')
    timeinput = input('Type offense time in format "00:00:00": ')
    calltypeinput = input('Type in the type of call: ')
    address = input('Type in the address (location) of the call: ')
    documentInsert = [
        {"OFFENSE_DATE": dateinput, "OFFENSE_TIME": timeinput, "CALL_TYPE": calltypeinput, "CITY": "San Jose", "STATE": "CA", "ADDRESS": address}]
    x = db.policeData.insert_many(documentInsert)
    if x.acknowledged:
        print("successfully inserted")
    else:
        print("something went wrong")

# function 2
def return_call_number():
    print('')
    print('--- Return Call Number  ---')
    dateinput = input('Type the date of the offense in format: "MM/DD/YYYY": ')
    typeinput = input('enter in the type of call: ')
    #myquery = {"OFFENSE_DATE": {"$lte": dateinput}, "OFFENSE_DATE":{"$lte": dateinput},
    #"CALL_TYPE":typeinput},{"CALL_NUMBER":1}
    mydoc = db.policeData.find({"OFFENSE_DATE": {"$lte": dateinput}, "OFFENSE_DATE":{"$lte": dateinput},
    "CALL_TYPE":typeinput},{"CALL_NUMBER":1, "CALL_TYPE":1})
    print_result(mydoc)

# function 3
def update_call():
    print("you pressed 3")

# Function 4
def return_call_details():
    print('')
    print('--- Call Details by Call Number ---')
    idInput = input("Type in the call number of the call: ")
    myquery = {"CALL_NUMBER": idInput}
    mydoc = db.policeData.find(myquery)
    print_result(mydoc)

# Function 5
def calls_by_date():
    print('')
    print('--- Calls by Offense Date ---')
    print("This query will take in a range of dates and return calls within the range.")
    gteInput = input("Enter start date in format: 'MM/DD/YYYY': ")
    lteInput = input("Enter end date in format: 'MM/DD/YYYY': ")
    choice = input("Would you like to narrow by OFFENSE_TIME? (Y/N): ")
    if str(choice).lower() == "y":
        time_start = input('Type start time in format "00:00:00": ')
        time_end = input('Type end time in format "00:00:00": ')
        myquery = {"OFFENSE_DATE": {"$gte": gteInput},
               "OFFENSE_DATE": {"$lte": lteInput},
               "OFFENSE_TIME": {"$gte": time_start},
               "OFFENSE_TIME": {"$lte": time_end},}
    else:
        myquery = {"OFFENSE_DATE": {"$gte": gteInput},
               "OFFENSE_DATE": {"$lte": lteInput}, }
    mydoc = db.policeData.find(myquery)
    print_result(mydoc)

# Function 6
def calls_by_emp():
    print('')
    print('--- Call Details per Employee ---')
    print("This query will take in employee ID and will return calls of that employee.")
    eidInput = input("Type in the employee ID: ")
    eidInput = int(eidInput)
    narrowByDate = input("Do you want to narrow the search by date? (Y/N): ")
    if (str(narrowByDate).lower() == "y"):
        start_date = input("Enter start date in format: 'MM/DD/YYYY': ")
        end_date = input("Enter end date in format: 'MM/DD/YYYY': ")
        myquery = {"EID": eidInput, "START_DATE": {
            "$gte": start_date}, "START_DATE": {"$lte": end_date}, }
    else:
        myquery = {"EID": eidInput}
    cur = db.policeData.find(myquery)
    print_result(cur)

# Function 7
def aggregate_calls_per_type():
    print('')
    print('--- Number of Calls per Type ---')
    start_date = input("Enter start date in format: 'MM/DD/YYYY': ")
    end_date = input("Enter end date in format: 'MM/DD/YYYY': ")
    query = [{
        "$match": {
            "OFFENSE_DATE": {
                "$gte": start_date,
                "$lt": end_date}
        }
    },
        {
            "$group": {"_id": "$CALL_TYPE", "count": {"$sum":1}}
    }
    ]
    cur = db.policeData.aggregate(query)
    for doc in cur:
        print(doc)

# Function 8
def aggregate_calls_per_day():
    print('')
    print('--- Number of Calls per Day ---')
    start_date = input("Enter start date in format: 'MM/DD/YYYY': ")
    end_date = input("Enter end date in format: 'MM/DD/YYYY': ")
    query = [{
        "$match": {
            "OFFENSE_DATE": {
                "$gte": start_date,
                "$lt": end_date}
        }
    },
        {
            "$group": {"_id": "$OFFENSE_DATE", "count": {"$sum":1}}
    }
    ]
    cur = db.policeData.aggregate(query)
    for doc in cur:
        print(doc)

# Function 9
def count_calls_by_priority():
    print('')
    print('--- Count Calls by Priotiy ---')
    start_date = input("Enter start date in format: 'MM/DD/YYYY': ")
    end_date = input("Enter end date in format: 'MM/DD/YYYY': ")
    query = [{
        "$match": {
            "OFFENSE_DATE": {
                "$gte": start_date,
                "$lt": end_date}
        }
    },
        {
            "$group": {"_id": "$PRIORITY", "count": {"$sum": 1}}
    }
    ]
    cur = db.policeData.aggregate(query)
    for doc in cur:
        print(doc)

# Function 10
def delete_calls_by_call_number():
    print('')
    print('--- DeleteCallsByNumber ---')
    print("Enter a call number to delete, or enter 'C' to cancel")
    choice = input("ENTER: ")
    if str(choice).lower() != 'c':
        # function
        print()
        print("loading...")
        print()
        myquery = {"CALL_NUMBER": str(choice)}
        cur = db.policeData.delete_many(myquery)
        if (cur.deleted_count) == 0:
            print("No calls that match that call number were found.")
        else:
            print('Successfully deleted ' + str(cur.deleted_count) + ' result')
        print()

def print_result(result):
    for doc in result:
        print(doc)

def cont_menu():
    choice = input("Enter any of key to return to menu: ")

# Open the connection
client = MongoClient("mongodb://54.198.141.68:27021")
db = client.police

q = False

while(not q):
    # Menu ---
    print('Police Call Data for the City of San Jose')
    print()
    print('Choose a function from the menu by entering the corresponding number')
    print('--- Menu ---')
    print('(1) RecordCall')
    print('(2) ReturnCallNumber')
    print('(3) UpdateCall')
    print('(4) ReturnCallDetails')
    print('(5) CallsbyDate')
    print('(6) CallsbyEmp')
    print('(7) AggregateCallsPerType')
    print('(8) AggregateCallsPerDay')
    print('(9) AverageCallsByType')
    print('(10) DeleteCallsByNumber')
    print("-------------")
    print()
    # --- end menu
    # get user choice
    user = input('Make a selection or enter (Q) to quit: ')
    # check for exit
    if str(user).lower() == 'q':
        q = True
    elif str(user) == '1':
        record_call()
        cont_menu()
    elif str(user) == '2':
        return_call_number()
        cont_menu()
    elif str(user) == '3':
        update_call()
        cont_menu()
    elif str(user) == '4':
        return_call_details()
        cont_menu()
    elif str(user) == '5':
        calls_by_date()
        cont_menu()
    elif str(user) == '6':
        calls_by_emp()
        cont_menu()
    elif str(user) == '7':
        aggregate_calls_per_type()
        cont_menu()
    elif str(user) == '8':
        aggregate_calls_per_day()
        cont_menu()
    elif str(user) == '9':
        count_calls_by_priority()
        cont_menu()
    elif str(user) == '10':
        delete_calls_by_call_number()
        cont_menu()

# close the connection
client.close()

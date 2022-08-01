from pymongo import MongoClient

# functions


def record_call():
    dateinput = input('Type start date in format: "MM/DD/YYYY": ')
    timeinput = input('Type time in format "00:00:00": ')
    calltypeinput = input('Type in the type of call: ')
    cityinput = input('Type in the city (location) of the call: ')
    documentInsert = [
        {"OFFENSE_DATE": dateinput, "OFFENSE_TIME": timeinput, "CALL_TYPE": calltypeinput, "CITY": cityinput}]
    x = db.policeData.insert_many(documentInsert)
    if x.acknowledged:
        print("successfully inserted")
    else:
        print("something went wrong")
    cont_menu()


def return_call_number():
    callTypeInput = input(
        'Please type the call type (STOLEN VEHICLE, PERSON DOWN,...): ')
    myquery = {"CALL_TYPE": callTypeInput}
    mydoc = db.policeData.find(myquery)
    cont_menu()


def update_call():
    print("you pressed 3")


def return_call_details():
    idInput = input("Type in the ID of the call: ")
    myquery = {"_id": idInput}
    mydoc = db.policeData.find(myquery)


def calls_by_date():
    print("This query will take in starting and ending dates and return calls within the range.")
    gteInput = input("Type in starting date: ")
    lteInput = input("Type in ending date: ")
    myquery = {"START_DATE": {"$gte": gteInput},
               "START_DATE": {"$lte": lteInput}, }
    mydoc = db.policeData.find(myquery)


def calls_by_emp():
    print("This query will take in employee ID and will return calls of that employee.")
    eidInput = input("Type in the employee ID: ")
    narrowByDate = input("Do you want to narrow the search by date? (Y/N)")
    if (narrowByDate == 'Y'):
        gteInput = input("Type in starting date: ")
        lteInput = input("Type in ending date: ")
        myquery = {"EID": eidInput, "START_DATE": {
            "$gte": gteInput}, "START_DATE": {"$lte": lteInput}, }
        mydoc = db.policeData.find(myquery)


def aggregate_calls_per_type():
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
            "$group": {"_id": "$CALL_TYPE", "count": {"$sum":1}}
    }
    ]
    cur = db.policeData.aggregate(query)
    for doc in cur:
        print(doc)


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

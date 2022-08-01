
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
        print("function 1")

def record_call():
    print("Hello from a function")

def return_call_number():
    print("Hello from a function")

def update_call():
    print("Hello from a function")

def return_call_details():
    print("Hello from a function")

def calls_by_date():
    print("Hello from a function")

def calls_by_emp():
    print("Hello from a function")

def aggregate_calls_per_day():
    print("Hello from a function")

def aggregate_calls_per_call_type():
    print("Hello from a function")

def delete_calls_by_type():
    print("Hello from a function")

def delte_calls_by_call_number():
    print("Hello from a function")
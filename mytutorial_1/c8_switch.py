# Switcher for implement  switch case option
def employee_details(ID):
    switcher = {
        "1004": "Employee Name: MD. Mehrab",
        "1009": "Employee Name: Mita Rahman",
        "1010": "Employee Name: Sakib Al Hasan",
    }
    '''The first argument will be returned if the match 
    found and nothing will be returened if no match found'''
    return switcher.get(ID, "Employee ID:%s Is Not Found" %ID)


# Take the employee ID
ID = input("Enter the employee ID: ")
# Print the output
print(employee_details(ID))

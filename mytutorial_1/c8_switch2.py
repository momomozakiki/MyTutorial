#!/usr/bin/env python3
# Take ID value as input
id = input("Enter your ID:\n")


# Define function to get grade value
def result(id):
    switcher = {
        "1001": "A+",
        "1002": "B+",
        "1004": "C+"
    }
    # return switcher.get(id, "Invalid")
    return switcher.get(id)


# Check the grade value
# if result(id) != "Invalid":
if result(id) is not None:

    # name are grade are keyword parameters
    print('{name} got {grade}'.format(name=id, grade=result(id)))

else:
    # One positional parameter and another keyword parameter.
    print('{0} got {grade}'.format(id, grade="F"))

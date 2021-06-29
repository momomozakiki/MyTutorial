'''
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
'''

'''
try:
    inp: str = input()
    print ('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
else:
    print ('No exception occurred')
'''

'''
# Zero Division Exception
try:
    a = 100 / 0
    print(a)
except ZeroDivisionError:
    print("Zero Division Exception Raised.")
else:
    print("Success, no error!")

# OverFlow Error
try:
    import math

    print(math.exp(1000))
except OverflowError:
    print("OverFlow Exception Raised.")
else:
    print("Success, no error!")
'''
# Assertion Error
try:
    a = 100
    b = "DataCamp"
    assert a == b
except AssertionError:
    print("Assertion Exception Raised.")
else:
    print("Success, no error!")

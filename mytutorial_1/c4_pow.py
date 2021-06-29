import math

# Assign values to x and n
x = 4
n = 3

# Method 1
power = x ** n
print('%d to the power %d is %d' % (x, n, power))

# Method 2
power = pow(x, n)
print('%d to the power %d is %0.3f' % (x, n, power))

# Method 3
power = math.pow(2, 6.5)
print('%d to the power %d is %5.2f' % (x, n, power))

# https://stackoverflow.com/questions/10282674/difference-between-the-built-in-pow-and-math-pow-for-floats-in-python/10282852
